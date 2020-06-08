from generator import *

category_all = DocCategory()
category_colors = DocCategory(title="Color Items")

doc_item_colors = DocCategoryItem("Colors", None, "Constants")
doc_item_colors.short_description = "A list of colors"
doc_item_colors.pre_text = DocumentPartial("items/colors_pretext.part.md")

doc_item_tgcolor = DocCategoryItem("TGColor", "Describes a color", "Struct")
doc_item_tgcolor.short_description = "The color structure"
doc_item_tgcolor.table.add(('id','unsigned int','Color ID'))
doc_item_tgcolor.table.add(('Foreground','unsigned short','Foreground color ID'))
doc_item_tgcolor.table.add(('Background','unsigned short','Backgorund color ID'))

doc_item_tgcolorcreate = DocCategoryItem("TGColorCreate", None, "Function")
doc_item_tgcolorcreate.short_description = "Create a color (pair)"
doc_item_tgcolorcreate.pre_text = DocumentPartial("items/createcolor_pretext.part.md")
doc_item_tgcolorcreate.table.add(('Foreground', 'int', 'Foreground color ID'))
doc_item_tgcolorcreate.table.add(('Background', 'int', 'Background color ID'))
doc_item_tgcolorcreate.post_text = "**Return Value**: `TGColor` struct\n"

category_all.add(doc_item_colors)
category_all.add(doc_item_tgcolor)
category_all.add(doc_item_tgcolorcreate)

category_colors.add(doc_item_colors)
category_colors.add(doc_item_tgcolor)
category_colors.add(doc_item_tgcolorcreate)

category_all.sort()
category_colors.sort()