; Author: Bu Kun
; Title: Display layers by attribute category


# Display layers by attribute category

In the previous example, the layers consisted of a set of features from the same dataset, rendered using the same style. However, you may not want to plot all features contained in a given dataset, or you may not want to plot all features in the same way. For example, making a world map containing all the roads for each dataset would take quite a while and the resulting map would be too cluttered to be very useful. The same symbols are used to render maps produced by country roads and highways, and there is no distinction between graphical functions; in the real world, the difference is obvious.

## View the map

Classes allow you to distinguish between features based on attributes and features based on classes.
The previous diagram uses classes because each layer must have at least one class.
At its simplest, the default class includes every feature of the dataset.
In this case, the layer has a class and each feature in that class is rendered in the same way.

However, you usually want to avoid using only the default classes and choose classification features instead, for the two reasons mentioned earlier:
First of all, you may not want to draw each feature, 
and second, you may want to use different symbols, colors or sizes to present some features with different attributes.

By using non-spatial attribute information in the data, you can create a map like this:

<div align="center">
<img class="img_border" src="{SITE_URL}/cgi-bin/mapserv?map=/owg/mfk3.map&layer=country&layer=weq&mode=map" />
</div>

or:

<div align="center">
<img class="img_border" src="{SITE_URL}/cgi-bin/mapserv?map=/owg/mfa3.map&layer=states_poly&layer=states_line&mode=map" />
</div>

## Map file

Here is the map file MapFile ( ``mfa3.map`` ):

->-> mfa3.map


<small>Mapfile for layer classification</small>

The structure of the map file, through the object, looks like this

<pre>
                                  MAP
      (states_poly) LAYER----------|---------LAYER (states_line)
                      |                      |
       (land) CLASS---|---CLASS (water)      |-CLASS
                  |       |                    |
            STYLE-|       |-STYLE              |-STYLE
</pre>

The changes in the documents are as follows:

->-> xx_diff_mfa3_mfa2.htmp

## Attribute description in Mapfile


MapFile still has only two layers, but polygon layers are subdivided into two broad categories. Take a look at the additional parameters:

    CLASSITEM "NAME"

This keyword is used to specify which properties are used by the detached class object. In this example, the property is ``NAME`` .
If you open the Shapefile of the database file associated with the attribute, you will see that there is a column (property) called ``NAME`` .


The easiest (and fastest) way to define a class using an expression to determine which MapServer the class contains is to use a string comparison. You can use the hierarchy keyword ``CLASSITEM`` to identify the attribute name that will be used for the classification function. Then specify that the comparison string is expressed using class-level keywords. It is good practice to quote strings to ensure that characters are interpreted correctly. This is shown in the code snippet below.
The ``CLASSITEM`` attribute expresses the value of the string that will be associated with each feature of the dataset. If the expression string matches the same ``CLASSITEM`` value, the function will be included in this class. Although fast and easy to use, this method is not very flexible, since the specified string expression must be passed through ``CLASSITEM`` to determine the matching attribute value.

    12         CLASSITEM "NAME"
    13         CLASS
    14             NAME "China"
    15             EXPRESSION "CHINA"
    16             STYLE
    17                 COLOR 232 30 30
    18             END
    19         END
    20         CLASS
    21             NAME "Others"
    22             STYLE
    23                 COLOR 198 198 255
    24             END
    25         END



Shapefile database records are stored in DBF files. You can open a spreadsheet program like Openoffice.org Compute, or a GIS software such as QGIS on the desktop. If the data has metadata (as it should), it can be known from the content of the metadata file. You can also use ``ogrinfo`` to display basic property information in a Shapefile - look back at Example 1.1 (after the last few lines, "LayerSRS WKT:" displays property names and types).


    EXPRESSION "CHINA"

For each class, specify the property value to use. This is the simplest form of expression.
Expressions can be more complex than this, allowing a regular comparison expression or logical expression.


## Classification based on comparative expressions

Allows for the classification of more complex functions, based on a logical expression of one or more attribute values.
``CLASSITEM`` does not need to be specified (actually, it will be ignored if so far). Keyword expressions introduce logical expressions, which are delimited within parentheses. The syntax is simple: a logical expression consists of the property name enclosed in square brackets, a comparison operator and the value. For example, the following code compares the number of values attributed to the population with the value 100000:

    EXPRESSION ( [POPULATION] < 100000 )

It will include a feature with less than 100,000 population attribute values. Like C and Perl, MapServer uses different comparisons for strings as well as comparisons for numbers, and you have to take care of observing the differences. If an attribute is a string value, then its reference must be enclosed in quotes and the values must be compared. Both single and double quotes can be used, but they must match. Consider the following code:

    EXPRESSION ( '[STATE_FIPS]' eq 'MN' )

This will include a feature only if this value attribute ` ` state_ FIPS ` ` is equal to the string Mn. Logical expressions can be combined using conjunctions and separation operators and or. Consider the following example:

    EXPRESSION (( [POPULATION] < 100000 ) and ( '[STATE_FIPS]' eq 'MN' ))

This matches features with populations less than 100000 ``STATE_FIPS`` equal to MN.

Note that confusion may occur if a string-valued property contains numeric strings (eg ``"123"`` ). If you compare strings-valued properties numerically, there will never be a match ( ``123`` will never be equal to ``"123"`` ), and there will never be an error. You can learn more about data types.

Note that MapServer's mapping file reference documentation has a misspelled numeric "not equals" operator, and ``!=`` does not display an exclamation mark ( ``!`` ).


- Operator,  Data Type 
- ``!=``,   Numeric 
- ``=``,  Numeric 
- ``>``,   Numeric 
- ``<``, Numeric 
- ``>=``,  Numeric
- ``<=``,  Numeric 
- ``and``,  Logical 
- ``or``,  Logical 
- ``eq``,  String
- ``ge``,  String
-  ``gt``, String
-  ``le``, String
- ``lt``, String
- ``ne``,  String


Note that although a class must be defined with a single method, each class can use a different method at a level.
