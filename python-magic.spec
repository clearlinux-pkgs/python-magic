#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-magic
Version  : 0.4.22
Release  : 38
URL      : https://github.com/ahupp/python-magic/archive/0.4.22/python-magic-0.4.22.tar.gz
Source0  : https://github.com/ahupp/python-magic/archive/0.4.22/python-magic-0.4.22.tar.gz
Summary  : File type identification using libmagic
Group    : Development/Tools
License  : MIT
Requires: python-magic-license = %{version}-%{release}
Requires: python-magic-python = %{version}-%{release}
Requires: python-magic-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : coverage
BuildRequires : file
BuildRequires : file-dev

%description
# python-magic
[![PyPI version](https://badge.fury.io/py/python-magic.svg)](https://badge.fury.io/py/python-magic)
[![Build Status](https://travis-ci.org/ahupp/python-magic.svg?branch=master)](https://travis-ci.org/ahupp/python-magic)

%package license
Summary: license components for the python-magic package.
Group: Default

%description license
license components for the python-magic package.


%package python
Summary: python components for the python-magic package.
Group: Default
Requires: python-magic-python3 = %{version}-%{release}

%description python
python components for the python-magic package.


%package python3
Summary: python3 components for the python-magic package.
Group: Default
Requires: python3-core
Provides: pypi(python_magic)

%description python3
python3 components for the python-magic package.


%prep
%setup -q -n python-magic-0.4.22
cd %{_builddir}/python-magic-0.4.22

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1613872242
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])")
export LC_ALL=en_US.UTF-8
python3 ./test/test.py || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-magic
cp %{_builddir}/python-magic-0.4.22/LICENSE %{buildroot}/usr/share/package-licenses/python-magic/73475ea543961f243b327f5e39ba5fc038f9770c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-magic/73475ea543961f243b327f5e39ba5fc038f9770c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
