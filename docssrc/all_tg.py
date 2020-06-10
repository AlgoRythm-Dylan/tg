from generator import *

category_all = DocCategory()
category_colors = DocCategory(title="Color Items")
category_buffer = DocCategory(title="Buffer Items")

doc_item_colors = DocItem("Colors", None, "Constants")
doc_item_colors.short_description = "A list of colors"
doc_item_colors.pre_text = DocumentPartial("items/colors_pretext.part.md")

doc_item_tgcolor = DocItem("TGColor", "Describes a color", "Struct")
doc_item_tgcolor.short_description = "The color structure"
doc_item_tgcolor.table.add(('id','unsigned int','Color ID'))
doc_item_tgcolor.table.add(('Foreground','unsigned short','Foreground color ID'))
doc_item_tgcolor.table.add(('Background','unsigned short','Backgorund color ID'))

doc_item_tgcolorcreate = DocItem("TGColorCreate", None, "Function")
doc_item_tgcolorcreate.short_description = "Create a color (pair)"
doc_item_tgcolorcreate.pre_text = DocumentPartial("items/createcolor_pretext.part.md")
doc_item_tgcolorcreate.table.add(('Foreground', 'int', 'Foreground color ID'))
doc_item_tgcolorcreate.table.add(('Background', 'int', 'Background color ID'))
doc_item_tgcolorcreate.post_text = "**Return Value**: `TGColor` struct\n"

doc_item_tgdefaultcolor = DocItem("TGDefaultColor", "A TGColor structure describing the console's default colors", "Extern")
doc_item_tgdefaultcolor.short_description = "The terminal's default color"

doc_item_tgcolornames = DocItem("TG_COLOR_NAMES", None, "Constant")
doc_item_tgcolornames.short_description = "A list of color names"
doc_item_tgcolornames.pre_text = DocumentPartial("items/colornames_pretext.part.md")

doc_item_tgbufaddlstring = DocItem("TGBufAddLString", ("Add a \"legacy string\" - one byte characters - at the " +
     "current buffer position (`virtualCursorPosition`) with the current buffer attributes."), "Function")
doc_item_tgbufaddlstring.short_description = "Add char* string"
doc_item_tgbufaddlstring.table.add(('Buffer', 'TGBuffer*', 'The buffer to draw to'))
doc_item_tgbufaddlstring.table.add(('str', 'char*', 'String to draw'))

doc_item_tgbufaddlstringattr = DocItem("TGBufAddLStringAttr", ("Add a \"legacy string\" - one byte characters - at " +
    " the current buffer position (`virtualCursorPosition`) with the attributes passed to the function."), "Function")
doc_item_tgbufaddlstringattr.short_description = "Add char* string with certain attributes"
doc_item_tgbufaddlstringattr.table.add(('Buffer', 'TGBuffer*', 'The buffer to draw to'))
doc_item_tgbufaddlstringattr.table.add(('str', 'char*', 'String to draw'))
doc_item_tgbufaddlstringattr.table.add(('attributes', 'TGAttributes', 'Attributes to use'))

doc_item_tgbufaddstring = DocItem("TGBufAddString", ("Add a wide string at the current buffer position " +
    "(virtualCursorPosition) with the current buffer attributes."), "Function")
doc_item_tgbufaddstring.short_description = "Add wchar_t* string"
doc_item_tgbufaddstring.table.add(('Buffer', 'TGBuffer*', 'The buffer to draw to'))
doc_item_tgbufaddstring.table.add(('str', 'wchar_t*', 'String to draw'))

doc_item_tgbufaddstringattr = DocItem("TGBufAddStringAttr", ("Add wide string at the current buffer position " + 
    "(virtualCursorPosition) with the attributes passed to the function."), "Function")
doc_item_tgbufaddstringattr.short_description = "Add wchar_t* string with certain attributes"
doc_item_tgbufaddstringattr.table.add(('Buffer', 'TGBuffer*', 'The buffer to draw to'))
doc_item_tgbufaddstringattr.table.add(('str', 'wchar_t*', 'String to draw'))
doc_item_tgbufaddstringattr.table.add(('attributes', 'TGAttributes', 'Attributes to use'))

doc_item_tgbufattr = DocItem("TGBufAttr", "Set’s a buffer's attributes at a specific location", "Function")
doc_item_tgbufattr.short_description = "Change attributes for a cell"
doc_item_tgbufattr.table.add(('Buffer', 'TGBuffer*', 'The buffer to draw to'))
doc_item_tgbufattr.table.add(('x', 'int', 'X position of the cell to update'))
doc_item_tgbufattr.table.add(('y', 'int', 'Y position of the cell to update'))
doc_item_tgbufattr.table.add(('Attributes', 'TGAttribtues', 'Attributes to set'))

doc_item_tgbufcell = DocItem("TGBufCell", "Set a cell's content", "Function")
doc_item_tgbufcell.short_description = "Set a cell's content"
doc_item_tgbufcell.table.add(('Buffer', 'TGBuffer*', 'The buffer to draw to'))
doc_item_tgbufcell.table.add(('x', 'int', 'X position of the cell to update'))
doc_item_tgbufcell.table.add(('y', 'int', 'Y position of the cell to update'))
doc_item_tgbufcell.table.add(('CharInfo', 'TGCharInfo', 'CharInfo to set'))

category_all.add(doc_item_colors)
category_all.add(doc_item_tgcolor)
category_all.add(doc_item_tgcolorcreate)
category_all.add(doc_item_tgdefaultcolor)
category_all.add(doc_item_tgcolornames)
category_all.add(doc_item_tgbufaddlstring)
category_all.add(doc_item_tgbufaddlstringattr)
category_all.add(doc_item_tgbufaddstring)
category_all.add(doc_item_tgbufaddstringattr)
category_all.add(doc_item_tgbufattr)
category_all.add(doc_item_tgbufcell)

category_colors.add(doc_item_colors)
category_colors.add(doc_item_tgcolor)
category_colors.add(doc_item_tgcolorcreate)
category_colors.add(doc_item_tgdefaultcolor)
category_colors.add(doc_item_tgcolornames)

category_buffer.add(doc_item_tgbufaddlstring)
category_buffer.add(doc_item_tgbufaddlstringattr)
category_buffer.add(doc_item_tgbufaddstring)
category_buffer.add(doc_item_tgbufaddstringattr)
category_buffer.add(doc_item_tgbufattr)
category_buffer.add(doc_item_tgbufcell)

category_all.sort()
category_colors.sort()
category_buffer.sort()