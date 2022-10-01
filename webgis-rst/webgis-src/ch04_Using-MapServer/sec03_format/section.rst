.. Author: Bu Kun .. Title: Change the output format of the map

Change the output format of the map
===================================

View examples
~~~~~~~~~~~~~

Depending on the format you choose, the image may not be displayed in
your browser. If the link doesn’t appear in your browser, right-click on
the image above to see what format is specified in MapFile for saving.

.. http://webgis.pub/cgi-bin/mapserv?map=/owg/mfa8.map&layers=land-shallow-topo+wcountry-line&map.imagetype=AGG&mode=map

.. figure:: http://webgis.pub/cgi-bin/mapserv?map=/owg/mfa8.map&layers=land-shallow-topo+wcountry-line&mode=map
   :alt: Different output results

   Different output results

Mapfile example
---------------

The following is the Mapfile used in this example ``mfa8.map`` ):


.. literalinclude:: ./mfa8.map
   :lineno-start: 1


Files are changed as follows:
-----------------------------

.. xx_diff_mfa8_mfa6.htmp


.. raw:: html

    <table class="diff" id="difflib_chg_to5__top"
           cellspacing="0" cellpadding="0" rules="groups" >
        <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup>
        <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup>
        <tbody>
            <tr><td class="diff_next" id="difflib_chg_to5__0"><a href="#difflib_chg_to5__0">f</a></td><td class="diff_header" id="from5_1">1</td><td nowrap="nowrap">MAP</td><td class="diff_next"><a href="#difflib_chg_to5__0">f</a></td><td class="diff_header" id="to5_1">1</td><td nowrap="nowrap">MAP</td></tr>
            <tr><td class="diff_next"><a href="#difflib_chg_to5__1">n</a></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"><a href="#difflib_chg_to5__1">n</a></td><td class="diff_header" id="to5_2">2</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;EXTENT&nbsp;-180&nbsp;-90&nbsp;180&nbsp;90</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_3">3</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;SIZE&nbsp;600&nbsp;300</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_4">4</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;SHAPEPATH&nbsp;"/gdata"</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_5">5</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;IMAGECOLOR&nbsp;0&nbsp;0&nbsp;255</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_6">6</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;FONTSET&nbsp;"../fonts/fonts.list"</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_7">7</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;SYMBOLSET&nbsp;"../symbols/symbols35.sym"</span></td></tr>
            <tr><td class="diff_next" id="difflib_chg_to5__1"></td><td class="diff_header" id="from5_2">2</td><td nowrap="nowrap">&nbsp;&nbsp;&nbsp;&nbsp;IMAGETYPE&nbsp;"PNG24"</td><td class="diff_next"></td><td class="diff_header" id="to5_8">8</td><td nowrap="nowrap">&nbsp;&nbsp;&nbsp;&nbsp;IMAGETYPE&nbsp;"PNG24"</td></tr>
            <tr><td class="diff_next"><a href="#difflib_chg_to5__2">n</a></td><td class="diff_header" id="from5_3">3</td><td nowrap="nowrap"><span class="diff_sub">&nbsp;&nbsp;&nbsp;&nbsp;EXTENT&nbsp;-20042150&nbsp;-7515806&nbsp;20104978&nbsp;7515807</span></td><td class="diff_next"><a href="#difflib_chg_to5__2">n</a></td><td class="diff_header" id="to5_9">9</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;OUTPUTFORMAT</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header" id="from5_4">4</td><td nowrap="nowrap"><span class="diff_sub">&nbsp;&nbsp;&nbsp;&nbsp;SIZE&nbsp;350&nbsp;260</span></td><td class="diff_next"></td><td class="diff_header" id="to5_10">10</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NAME&nbsp;"png8"</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header" id="from5_5">5</td><td nowrap="nowrap"><span class="diff_sub">&nbsp;&nbsp;&nbsp;&nbsp;SHAPEPATH&nbsp;"/gdata"</span></td><td class="diff_next"></td><td class="diff_header" id="to5_11">11</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DRIVER&nbsp;"AGG/PNG8"</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header" id="from5_6">6</td><td nowrap="nowrap"><span class="diff_sub">&nbsp;&nbsp;&nbsp;&nbsp;SYMBOLSET&nbsp;"../symbols/symbols35.sym"</span></td><td class="diff_next"></td><td class="diff_header" id="to5_12">12</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MIMETYPE&nbsp;"image/png;&nbsp;mode=8bit"</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header" id="from5_7">7</td><td nowrap="nowrap"><span class="diff_sub">&nbsp;&nbsp;&nbsp;&nbsp;FONTSET&nbsp;"../fonts/fonts.list"</span></td><td class="diff_next"></td><td class="diff_header" id="to5_13">13</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IMAGEMODE&nbsp;RGB</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header" id="from5_8">8</td><td nowrap="nowrap"><span class="diff_sub">&nbsp;&nbsp;&nbsp;&nbsp;PROJECTION</span></td><td class="diff_next"></td><td class="diff_header" id="to5_14">14</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EXTENSION&nbsp;"png"</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header" id="from5_9">9</td><td nowrap="nowrap"><span class="diff_sub">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"init=epsg:3857"</span></td><td class="diff_next"></td><td class="diff_header" id="to5_15">15</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FORMATOPTION&nbsp;"QUANTIZE_FORCE=on"</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_16">16</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FORMATOPTION&nbsp;"QUANTIZE_COLORS=256"</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_17">17</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FORMATOPTION&nbsp;"GAMMA=0.75"</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_18">18</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;END</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_19">19</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;OUTPUTFORMAT</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_20">20</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NAME&nbsp;"png"</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_21">21</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DRIVER&nbsp;"AGG/PNG"</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_22">22</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IMAGEMODE&nbsp;RGB</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_23">23</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;END</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_24">24</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;OUTPUTFORMAT</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_25">25</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NAME&nbsp;"png24"</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_26">26</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DRIVER&nbsp;"AGG/PNG"</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_27">27</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IMAGEMODE&nbsp;RGBA</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_28">28</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TRANSPARENT&nbsp;TRUE</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_29">29</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;END</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_30">30</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;OUTPUTFORMAT</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_31">31</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NAME&nbsp;"jpeg"</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_32">32</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DRIVER&nbsp;"AGG/JPEG"</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_33">33</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IMAGEMODE&nbsp;RGB</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_34">34</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;END</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_35">35</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;OUTPUTFORMAT</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_36">36</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NAME&nbsp;"svg"</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_37">37</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DRIVER&nbsp;"CAIRO/SVG"</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_38">38</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MIMETYPE&nbsp;"image/svg+xml"</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_39">39</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IMAGEMODE&nbsp;RGB</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_40">40</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EXTENSION&nbsp;"svg"</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_41">41</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;END</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_42">42</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;OUTPUTFORMAT</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_43">43</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NAME&nbsp;"pdf"</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_44">44</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DRIVER&nbsp;"CAIRO/PDF"</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_45">45</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MIMETYPE&nbsp;"application/x-pdf"</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_46">46</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IMAGEMODE&nbsp;RGB</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_47">47</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EXTENSION&nbsp;"pdf"</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_48">48</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;END</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_49">49</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;OUTPUTFORMAT</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_50">50</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NAME&nbsp;"cairopng"</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_51">51</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DRIVER&nbsp;"CAIRO/PNG"</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_52">52</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MIMETYPE&nbsp;"image/png"</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_53">53</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IMAGEMODE&nbsp;RGB</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_54">54</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EXTENSION&nbsp;"png"</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_55">55</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;END</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_56">56</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;OUTPUTFORMAT</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_57">57</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NAME&nbsp;"GTiff"</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_58">58</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DRIVER&nbsp;"GDAL/GTiff"</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_59">59</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MIMETYPE&nbsp;"image/tiff"</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_60">60</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IMAGEMODE&nbsp;RGB</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_61">61</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EXTENSION&nbsp;"tif"</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header" id="from5_10">10</td><td nowrap="nowrap">&nbsp;&nbsp;&nbsp;&nbsp;END</td><td class="diff_next"></td><td class="diff_header" id="to5_62">62</td><td nowrap="nowrap">&nbsp;&nbsp;&nbsp;&nbsp;END</td></tr>
        </tbody>
        <tbody>
            <tr><td class="diff_next" id="difflib_chg_to5__2"></td><td class="diff_header" id="from5_15">15</td><td nowrap="nowrap">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TYPE&nbsp;RASTER</td><td class="diff_next"></td><td class="diff_header" id="to5_67">67</td><td nowrap="nowrap">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TYPE&nbsp;RASTER</td></tr>
            <tr><td class="diff_next"><a href="#difflib_chg_to5__top">t</a></td><td class="diff_header" id="from5_16">16</td><td nowrap="nowrap"><span class="diff_sub">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PROJECTION</span></td><td class="diff_next"><a href="#difflib_chg_to5__top">t</a></td><td class="diff_header" id="to5_68">68</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;END</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header" id="from5_17">17</td><td nowrap="nowrap"><span class="diff_sub">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"init=epsg:4326"</span></td><td class="diff_next"></td><td class="diff_header" id="to5_69">69</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;LAYER</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_70">70</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NAME&nbsp;"wcountry-line"</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_71">71</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DATA&nbsp;"wcountry.shp"</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_72">72</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;STATUS&nbsp;OFF</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_73">73</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TYPE&nbsp;LINE</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_74">74</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CLASS</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_75">75</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NAME&nbsp;"State&nbsp;Boundary"</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_76">76</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;STYLE</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_77">77</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SYMBOL&nbsp;"line5"</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_78">78</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;COLOR&nbsp;255&nbsp;255&nbsp;0</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_79">79</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SIZE&nbsp;1</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header"></td><td nowrap="nowrap"></td><td class="diff_next"></td><td class="diff_header" id="to5_80">80</td><td nowrap="nowrap"><span class="diff_add">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;END</span></td></tr>
            <tr><td class="diff_next"></td><td class="diff_header" id="from5_18">18</td><td nowrap="nowrap">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;END</td><td class="diff_next"></td><td class="diff_header" id="to5_81">81</td><td nowrap="nowrap">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;END</td></tr>
        </tbody>
    </table>


Now our MapFile contains a new object ``OUTPUTFORMAT`` . Within the
``MAP`` object defined by this object, and when used with the keyword
``IMAGETYPE``.

Depending on the compiled library of MapServer, you can have a variety
of output formats to choose from - the GD library provides ``PNG``
(8-bit and 24-bit), ``GIF``, ``JPEG``, ``WBMP`` , the GDAL library,
which sources many of MapServer’s input formats, and can also provide
output in ``PNG``, ``JPEG``, ``TIFF/GeoTIFF``, and other raster formats;
the pdflib library provides PDF output.

.. raw:: html

   <!-- Mingku provides flash output -->

Have a look at your MAPFILE object by changing the keyword ``IMAGETYPE``
and experiment with ``OUTPUTFORMAT`` . It should be used as
``IMAGETYPE`` value (eg: ``IMAGETYPE png`` or ``PNG24 IMAGETYPE`` ), the
name of the output format.

Please consult the ``OUTPUTFORMAT`` object reference:

//www.mapserver.org/mapfile/outputformat.html#outputformat
