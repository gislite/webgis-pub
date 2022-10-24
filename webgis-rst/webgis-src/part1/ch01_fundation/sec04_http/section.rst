.. Author: Bu Kun .. Title: Principle and method of HTTP

Principle and method of HTTP
============================

WebGIS is based on Web technology, so we need to understand the basic
principles and methods of HTTP.

Different methods in HTTP
-------------------------

HTTP defines different methods of interacting with the server. There are
four basic methods: get, post, put and delete. The full name of URL is a
resource descriptor. We can think of it as follows: a URL address is
used to describe a resource on the network, and the get, post, put and
delete in HTTP correspond to the four operations of querying, modifying,
adding and deleting this resource. Here, you should have a general
understanding. Get is generally used to obtain / query resource
information, while post is generally used to update resource
information.

Idempotency of HTTP GET
~~~~~~~~~~~~~~~~~~~~~~~

According to the HTTP specification, GET is used for information
retrieval and should be safe and idempotent.

(1) Safe means that the operation is used to obtain information rather
    than modify it. In other words, GET requests should generally not
    have side effects. That is to say, it only obtains resource
    information, just like a database query, it will not modify or add
    data, and will not affect the state of the resource.

Note: The meaning of security here only refers to non-modified
information.

(2) Idempotent means that multiple requests to the same URL should
    return the same result. Here I will explain the concept of
    idempotency again: idempotent (idempotent, idempotence) is a
    mathematical or computer concept, common in abstract algebra.

Idempotency has the following definitions:

-  For unary operations, an operation is said to be idempotent if the
   result of performing the operation multiple times for all a number in
   the range is the same as the result of performing the operation once.
   For example, absolute value operation is an example. In the set of
   real numbers, there is ``abs(a)=abs(abs(a))``.

-  For binocular operation, it is required that when the two values
   involved in the operation are equivalent, if the operation result is
   equal to the two values involved in the operation, the operation is
   called idempotent. For example, the function for finding the maximum
   value of the two numbers is idempotent in the real number set, that
   is ``max (x, x) = x``. After reading the above explanation, you
   should be able to understand the meaning of GET idempotency. However,
   in practical application, the above two regulations are not so
   strict. An example of citing someone else’s article: For example, the
   front page of a news site is constantly updated. Although the second
   request returns a different batch of news, the operation is still
   considered safe and idempotent because it always returns the current
   news. Fundamentally, if the goal is that when a user opens a link, he
   can be confident that the resource has not changed from his own
   perspective.

POST method
~~~~~~~~~~~

According to the HTTP specification, POST represents a request that may
modify a resource on the server. Continue to cite the above example:
Take news as an example, readers should post their own comments on news,
because the resources of the site are different after the comments are
submitted, or the resources have been modified.

But in practice, many people do not follow the HTTP specification. There
are many reasons for this problem, such as:

1.Many people are greedy for convenience and use GET when updating
resources, because POST must go to the FORM (form), which will be a
little more troublesome.

2.The operations of adding, deleting, modifying and checking resources
can actually be done through ``GET/POST``, without using ``PUT`` and
``DELETE``.

3.Another is that early web framework designers did not consciously
treat and design URLs as abstract resources, so a serious problem is
that traditional web frameworks basically only support GET and POST.
HTTP methods are not supported for PUT and DELETE methods.

The above three points typically describe the old style (not strictly
abiding by the HTTP specification). With the development of the
architecture, REST (Representational State Transfer), a new style that
supports the HTTP specification, can refer to “RESTful Web Services”.

Difference between GET and POST in HTTP
---------------------------------------

After talking about the principle problem, let’s take a look at the
difference between GET and POST from the surface:

Submission form of the parameter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The data of the GET request will be attached to the URL (that is, the
data will be placed in the HTTP protocol header), the URL and the
transmission data are separated by ``?``, and the parameters are
connected by ``&``, such as:
``login. action name=hyddd&password=idontknow&verify=%E4%BD%A0%E5%A5%BD``.
If the data is English letters/numbers, send it as it is, if it is a
space, convert it to +, if it is Chinese/other characters, directly
encrypt the string with BASE64, and get such as: %E4%BD%A0%E5%A5% BD,
where XX in %XX is the ASCII hex representation of the symbol.

POST places the submitted data in the body of the HTTP package.

Restrictions on submitting parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The limit of data bytes submitted by GET method, and the limit of POST.
In fact, this is conditional:

(1) Because GET submits data through a URL, the amount of data that GET
    can submit is directly related to the length of the URL. In fact,
    there is no upper limit of parameters for URLs, and the HTTP
    protocol specification does not limit the length of URLs. This
    restriction is a particular browser and server restriction on it.
    IE’s limit on URL length is 2083 bytes (2K+35). For other browsers,
    such as Netscape, FireFox, etc., there is no length limit in theory,
    and the limit depends on the support of the operating system.

Note that this is limited to the entire URL length, not just the data
length of your parameter values.

(2) In theory, there is no size limit for POST, and no size limit for
    the HTTP protocol specification. It is inaccurate to say that “the
    POST data volume has a size limit of 80K/100K”, and no limit to the
    POST data. The role is the processing power of the server’s handler.

For ASP programs, there is a 100K data length limit when the Request
object processes each form field. But if you use Request.BinaryRead
there is no such restriction.

From this extension, Microsoft has increased the restrictions on IIS
6.0for security reasons.

So the above 80K and 100K may just be the default values (Note: I have
not confirmed the parameters of IIS4 and IIS5), but they can definitely
be set by yourself. Since each version of IIS has different default
values for these parameters, please refer to the relevant IIS
configuration documents for details.

Data submission security issues
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

POST is more secure than GET. Note: The security mentioned here is not
the same concept as the “security” mentioned in GET above. The meaning
of “security” above is only not to modify data, and the meaning of
security here is the meaning of real Security, such as: submitting data
through GET, the user name and password will appear on the URL in plain
text, because (1) the login page may be accessed by Browser cache, (2)
Others view the browser’s history, then others can get your account and
password. In addition, using GET to submit data may also cause a
Cross-site request forgery attack.

To sum up, ``GET`` is a request to the server for data, while ``Post``
is a request to submit data to the server. In the FORM (form), the
Method defaults to “GET”. Above, GET and POST are just different sending
mechanisms, not one fetching and one sending. This is also evident in
MapServer applications, where MapServer requests can be submitted using
``GET`` or ``POST``.
