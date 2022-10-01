; Author: Bu Kun
; Title: Add legend

# Add Legend

The map legend of MapServer can be added to or separated from the map.

## Effect

<p align="center">
<img class= "img_border" src="http://webgis.pub/cgi-bin/mapserv?map=/owg/mfa9.map&layer=states&layer=states_label&layer=topo&mode=map" />
</p>


## Key code

    LEGEND
    STATUS embed
    IMAGECOLOR 230 230 230
    LABEL
    TYPE truetype
    FONT "arial"
    COLOR 0 0 0
    SIZE 10
    ANTIALIAS true
    END
    END

    
Where ``STATUS`` is set to ``embed`` , which can be directly mosaicked into the generated map.