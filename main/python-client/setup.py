"""
    Tpay.com Technical Documentation

     <p class=\"changes-disclaimer\"> Demo transaction/masspayments api key: <input type=\"text\" id=\"transaction_key\" value=\"75f86137a6635df826e3efe2e66f7c9a946fdde1\" class=\"ui-form-control\"/><label for=\"transaction_key\" style=\"display: none;\" id=\"tr_api_label\">COPIED!</label><br/><br/> Demo cards api key: <input type=\"text\" id=\"cards_key\" value=\"ba9a05faa697f9b43f39b84933ff168e373c6496\" class=\"ui-form-control\"/><label for=\"cards_key\" style=\"display: none;\" id=\"cards_api_label\">COPIED!</label><br/><br/> Demo registration api key: <input type=\"text\" id=\"registration_key\" value=\"6c0f5ef6e4d6877abad7fcfb3b5de117ad8b772d\" class=\"ui-form-control\"/><label for=\"registration_key\" style=\"display: none;\" id=\"registration_api_label\">COPIED!</label><br/><br/> The terms seller and merchant are used interchangeably and they both refer to a person or a company registered at tpay.com to accept online payments. <br/> Whenever term merchant panel is used it refers to the part of tpay.com website located at <a href=\"https://secure.tpay.com/panel\" target=\"_blank\">secure.tpay.com/panel</a>. <br/><br/> For sandbox purposes use merchant demo account <br/><br/> ID - 1010, Password - demo<br/><br/>Remember that this is a shared account, so all data passed through will be publicly visible.</p>  # noqa: E501

    The version of the OpenAPI document: 1.1.3
    Contact: pt@tpay.com
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "openapi-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="Tpay.com Technical Documentation",
    author="OpenAPI Generator community",
    author_email="pt@tpay.com",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Tpay.com Technical Documentation"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
     &lt;p class&#x3D;\&quot;changes-disclaimer\&quot;&gt; Demo transaction/masspayments api key: &lt;input type&#x3D;\&quot;text\&quot; id&#x3D;\&quot;transaction_key\&quot; value&#x3D;\&quot;75f86137a6635df826e3efe2e66f7c9a946fdde1\&quot; class&#x3D;\&quot;ui-form-control\&quot;/&gt;&lt;label for&#x3D;\&quot;transaction_key\&quot; style&#x3D;\&quot;display: none;\&quot; id&#x3D;\&quot;tr_api_label\&quot;&gt;COPIED!&lt;/label&gt;&lt;br/&gt;&lt;br/&gt; Demo cards api key: &lt;input type&#x3D;\&quot;text\&quot; id&#x3D;\&quot;cards_key\&quot; value&#x3D;\&quot;ba9a05faa697f9b43f39b84933ff168e373c6496\&quot; class&#x3D;\&quot;ui-form-control\&quot;/&gt;&lt;label for&#x3D;\&quot;cards_key\&quot; style&#x3D;\&quot;display: none;\&quot; id&#x3D;\&quot;cards_api_label\&quot;&gt;COPIED!&lt;/label&gt;&lt;br/&gt;&lt;br/&gt; Demo registration api key: &lt;input type&#x3D;\&quot;text\&quot; id&#x3D;\&quot;registration_key\&quot; value&#x3D;\&quot;6c0f5ef6e4d6877abad7fcfb3b5de117ad8b772d\&quot; class&#x3D;\&quot;ui-form-control\&quot;/&gt;&lt;label for&#x3D;\&quot;registration_key\&quot; style&#x3D;\&quot;display: none;\&quot; id&#x3D;\&quot;registration_api_label\&quot;&gt;COPIED!&lt;/label&gt;&lt;br/&gt;&lt;br/&gt; The terms seller and merchant are used interchangeably and they both refer to a person or a company registered at tpay.com to accept online payments. &lt;br/&gt; Whenever term merchant panel is used it refers to the part of tpay.com website located at &lt;a href&#x3D;\&quot;https://secure.tpay.com/panel\&quot; target&#x3D;\&quot;_blank\&quot;&gt;secure.tpay.com/panel&lt;/a&gt;. &lt;br/&gt;&lt;br/&gt; For sandbox purposes use merchant demo account &lt;br/&gt;&lt;br/&gt; ID - 1010, Password - demo&lt;br/&gt;&lt;br/&gt;Remember that this is a shared account, so all data passed through will be publicly visible.&lt;/p&gt;  # noqa: E501
    """
)
