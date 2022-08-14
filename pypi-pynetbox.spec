#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pynetbox
Version  : 6.6.2
Release  : 5
URL      : https://files.pythonhosted.org/packages/ea/c6/269711c733eaf100e70877cc1a6bc9a19747d070f5c257479afb9d4e3ffb/pynetbox-6.6.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/ea/c6/269711c733eaf100e70877cc1a6bc9a19747d070f5c257479afb9d4e3ffb/pynetbox-6.6.2.tar.gz
Summary  : NetBox API client library
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-pynetbox-license = %{version}-%{release}
Requires: pypi-pynetbox-python = %{version}-%{release}
Requires: pypi-pynetbox-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(requests)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(six)

%description
# Pynetbox
Python API client library for [NetBox](https://github.com/netbox-community/netbox).

%package license
Summary: license components for the pypi-pynetbox package.
Group: Default

%description license
license components for the pypi-pynetbox package.


%package python
Summary: python components for the pypi-pynetbox package.
Group: Default
Requires: pypi-pynetbox-python3 = %{version}-%{release}

%description python
python components for the pypi-pynetbox package.


%package python3
Summary: python3 components for the pypi-pynetbox package.
Group: Default
Requires: python3-core
Provides: pypi(pynetbox)
Requires: pypi(requests)
Requires: pypi(six)

%description python3
python3 components for the pypi-pynetbox package.


%prep
%setup -q -n pynetbox-6.6.2
cd %{_builddir}/pynetbox-6.6.2
pushd ..
cp -a pynetbox-6.6.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656398876
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pynetbox
cp %{_builddir}/pynetbox-6.6.2/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pynetbox/3769fdac4576ae4dcecac765ba9b6c3b065d7849
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pynetbox/3769fdac4576ae4dcecac765ba9b6c3b065d7849

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
