=======================================================
MapServer interaction: layer control
=======================================================


- Author: bukun
- Update: 2022-10-7

How to control layers
=======================================================

Being able to turn map layers on and off is a standard feature of web mapping applications.
There are many ways to accomplish this using form objects as control.
You can use the drop box/menu, check boxes, and/or radio buttons.
In this example you'll see how to implement layer selection using check boxes and drop boxes.</p>

Here is the corresponding Mapfile:

.. literalinclude:: ./mfu3.map
   :lineno-start: 1


Notice how the layer STATUS has been changed to OFF except for the &quot;States&quot;
polygon background. The states background was left as default so our map will always have something
when drawn without any layers turned on. 
The users of our application should have control of which layers to turn on or leave off.</p>

You'll understand how the layers are turned on/off by MapServ if you look at the:

::

    <form method="get" action="/cgi-bin/mapserv" role="form">
        <fieldset>
            <legend>Layer control form</legend>
            <br>
            <!-- The following two variables are user defined variables.
                 MapServer will pass its value to the HTML template if the
                 proper tags are found, in square brackets "[]"  -->
            <input type="hidden" name="root" value="/owg">
            <input type="hidden" name="program" value="/cgi-bin/mapserv">
            <!-- The map and layer variables are internal MapServer variables.
                 They are required by the mapping application. -->
            <input type="hidden" name="map" value="/owg/mfu3.map">
            <input type="hidden" name="layer" value="states_poly">
            <input type="hidden" name="zoom" value="0">
            <!-- The map_web_template variable will replace the TEMPLATE
                 parameter in the WEB object of the MAP file... -->
            <div class="col-sm-12">
                <div class="col-sm-3">
                    <select name="map_web" class="form-control">
                        <option value="template tmpl-example-u3.html">Layer control</option>
                    </select>
                </div>
                <div class="col-sm-2">
                    <input type="submit" name="submit" value="Open the tutorial" class="btn btn-primary">
                </div>
            </div>
        </fieldset>
    </form>


## Open and close map layers

The demo could be opened directly via the following link:

::

    <a href="/cgi-bin/mapserv?map=/owg/mfu3.map&layer=states_line&zoom=0&mode=browse&root=/mstuto&program=/cgi-bin/mapserv&map_web=template+tmpl-example-u3.html"
               target="_blank">Open layer control page</a>
    <hr/>

The following shows a form submission, and various parameters are passed through the hidden `input` control. The effect is the same as above：

::

    <form method="get" action="/cgi-bin/mapserv" role="form">
        <fieldset>
            <legend>Layer control form</legend>
            <br>
            <!-- The following two variables are user defined variables.
                 MapServer will pass its value to the HTML template if the
                 proper tags are found, in square brackets "[]"  -->
            <input type="hidden" name="root" value="/owg">
            <input type="hidden" name="program" value="/cgi-bin/mapserv">
            <!-- The map and layer variables are internal MapServer variables.
                 They are required by the mapping application. -->
            <input type="hidden" name="map" value="/owg/mfu3.map">
            <input type="hidden" name="layer" value="states_poly">
            <input type="hidden" name="zoom" value="0">
            <!-- The map_web_template variable will replace the TEMPLATE
                 parameter in the WEB object of the MAP file... -->
            <div class="col-sm-12">
                <div class="col-sm-3">
                    <select name="map_web" class="form-control">
                        <option value="template tmpl-example-u3.html">Layer control</option>
                    </select>
                </div>
                <div class="col-sm-2">
                    <input type="submit" name="submit" value="Open the tutorial" class="btn btn-primary">
                </div>
            </div>
        </fieldset>
    </form>
