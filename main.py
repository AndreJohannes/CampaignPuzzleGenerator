import cairo
import json

import get_donors
import make_flags
import make_puzzle
import make_source
import make_template
import make_tiling

res = (733, 915)
nx = 30
ny = 40
print "Get Donor List"
donor_manager = get_donors.Donors()
has_new = donor_manager.has_new()
if has_new:
    donors = (get_donors.Donors()).get_donors()
    print "Make tiling"
    tiling = (make_tiling.Tiling()).make(nx, ny, donors)
    print "Make image"
    image = make_source.Source().make(nx, ny, tiling, res)
    print "Make flags"
    flags = (make_flags.Source()).make(nx, ny, tiling, res)
    print "Get mask"
    mask = cairo.ImageSurface.create_from_png("image/mask_{}x{}.png".format(nx, ny))
    print "Make template"
    template = make_template.Template().make(nx, ny, image, flags, mask, res)
    template.write_to_png("image/template_{}x{}.png".format(nx, ny))
    print "Compose"
    surface1, surface2 = make_puzzle.Compose().make(nx, ny, template, res)
    surface1.write_to_png("image/puzzle_{}x{}.png".format(nx, ny))
    surface2.write_to_png("image/flags_{}x{}.png".format(nx, ny))

    with open('./json/donors.json', 'w') as outfile:
        data = []
        for row in tiling:
            data_row = []
            data.append(data_row)
            for element in row:
                if element is None:
                    data_row.append(None)
                else:
                    data_row.append({"name":element["name"],"country":element["country"]})

        json.dump(data, outfile)

else:
    print("Nothing new. Exiting.")
