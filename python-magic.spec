#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-magic
Version  : 0.4.15
Release  : 13
URL      : https://github.com/ahupp/python-magic/archive/0.4.15.tar.gz
Source0  : https://github.com/ahupp/python-magic/archive/0.4.15.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: python-magic-python3
Requires: python-magic-python
BuildRequires : file
BuildRequires : file-dev
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
# python-magic
[![PyPI version](https://badge.fury.io/py/python-magic.svg)](https://badge.fury.io/py/python-magic)
[![Build Status](https://travis-ci.org/ahupp/python-magic.svg?branch=master)](https://travis-ci.org/ahupp/python-magic)

%package python
Summary: python components for the python-magic package.
Group: Default
Requires: python-magic-python3

%description python
python components for the python-magic package.


%package python3
Summary: python3 components for the python-magic package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-magic package.


%prep
%setup -q -n python-magic-0.4.15

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523299416
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test || :
%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
