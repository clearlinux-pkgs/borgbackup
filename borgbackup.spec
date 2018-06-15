#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x243ACFA951F78E01 (tw-public@gmx.de)
#
Name     : borgbackup
Version  : 1.1.5
Release  : 7
URL      : https://github.com/borgbackup/borg/releases/download/1.1.5/borgbackup-1.1.5.tar.gz
Source0  : https://github.com/borgbackup/borg/releases/download/1.1.5/borgbackup-1.1.5.tar.gz
Source99 : https://github.com/borgbackup/borg/releases/download/1.1.5/borgbackup-1.1.5.tar.gz.asc
Summary  : Deduplicated, encrypted, authenticated and compressed backups
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause CC0-1.0
Requires: borgbackup-bin
Requires: borgbackup-python3
Requires: borgbackup-license
Requires: borgbackup-python
Requires: msgpack-python
BuildRequires : acl-dev
BuildRequires : lz4-dev
BuildRequires : msgpack-python
BuildRequires : openssl-dev
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools_scm
BuildRequires : tox
BuildRequires : virtualenv
BuildRequires : zstd-dev

%description
Here we store 3rd party documentation, licenses, etc.
Please note that all files inside the "borg" package directory (except the
stuff excluded in setup.py) will be INSTALLED, so don't keep docs or licenses
there.

%package bin
Summary: bin components for the borgbackup package.
Group: Binaries
Requires: borgbackup-license

%description bin
bin components for the borgbackup package.


%package license
Summary: license components for the borgbackup package.
Group: Default

%description license
license components for the borgbackup package.


%package python
Summary: python components for the borgbackup package.
Group: Default
Requires: borgbackup-python3

%description python
python components for the borgbackup package.


%package python3
Summary: python3 components for the borgbackup package.
Group: Default
Requires: python3-core

%description python3
python3 components for the borgbackup package.


%prep
%setup -q -n borgbackup-1.1.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1529093811
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/borgbackup
cp LICENSE %{buildroot}/usr/share/doc/borgbackup/LICENSE
cp docs/3rd_party/lz4/LICENSE %{buildroot}/usr/share/doc/borgbackup/docs_3rd_party_lz4_LICENSE
cp docs/3rd_party/zstd/LICENSE %{buildroot}/usr/share/doc/borgbackup/docs_3rd_party_zstd_LICENSE
cp docs/3rd_party/blake2/COPYING %{buildroot}/usr/share/doc/borgbackup/docs_3rd_party_blake2_COPYING
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/borg
/usr/bin/borgfs

%files license
%defattr(-,root,root,-)
/usr/share/doc/borgbackup/LICENSE
/usr/share/doc/borgbackup/docs_3rd_party_blake2_COPYING
/usr/share/doc/borgbackup/docs_3rd_party_lz4_LICENSE
/usr/share/doc/borgbackup/docs_3rd_party_zstd_LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
