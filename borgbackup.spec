#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x243ACFA951F78E01 (tw-public@gmx.de)
#
Name     : borgbackup
Version  : 1.1.8
Release  : 22
URL      : https://github.com/borgbackup/borg/releases/download/1.1.8/borgbackup-1.1.8.tar.gz
Source0  : https://github.com/borgbackup/borg/releases/download/1.1.8/borgbackup-1.1.8.tar.gz
Source99 : https://github.com/borgbackup/borg/releases/download/1.1.8/borgbackup-1.1.8.tar.gz.asc
Summary  : Deduplicated, encrypted, authenticated and compressed backups
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause CC0-1.0
Requires: borgbackup-bin = %{version}-%{release}
Requires: borgbackup-license = %{version}-%{release}
Requires: borgbackup-python = %{version}-%{release}
Requires: borgbackup-python3 = %{version}-%{release}
Requires: llfuse
Requires: msgpack
BuildRequires : acl-dev
BuildRequires : buildreq-distutils3
BuildRequires : lz4-dev
BuildRequires : openssl-dev
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools_scm
BuildRequires : tox
BuildRequires : virtualenv
BuildRequires : zstd-dev
Patch1: 0001-fix-msgpack-version-reqs.patch

%description
What is BorgBackup?
        -------------------

%package bin
Summary: bin components for the borgbackup package.
Group: Binaries
Requires: borgbackup-license = %{version}-%{release}

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
Requires: borgbackup-python3 = %{version}-%{release}

%description python
python components for the borgbackup package.


%package python3
Summary: python3 components for the borgbackup package.
Group: Default
Requires: python3-core

%description python3
python3 components for the borgbackup package.


%prep
%setup -q -n borgbackup-1.1.8
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1544334433
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/borgbackup
cp LICENSE %{buildroot}/usr/share/package-licenses/borgbackup/LICENSE
cp docs/3rd_party/blake2/COPYING %{buildroot}/usr/share/package-licenses/borgbackup/docs_3rd_party_blake2_COPYING
cp docs/3rd_party/lz4/LICENSE %{buildroot}/usr/share/package-licenses/borgbackup/docs_3rd_party_lz4_LICENSE
cp docs/3rd_party/zstd/LICENSE %{buildroot}/usr/share/package-licenses/borgbackup/docs_3rd_party_zstd_LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
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
%defattr(0644,root,root,0755)
/usr/share/package-licenses/borgbackup/LICENSE
/usr/share/package-licenses/borgbackup/docs_3rd_party_blake2_COPYING
/usr/share/package-licenses/borgbackup/docs_3rd_party_lz4_LICENSE
/usr/share/package-licenses/borgbackup/docs_3rd_party_zstd_LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
