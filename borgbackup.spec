#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x243ACFA951F78E01 (tw-public@gmx.de)
#
Name     : borgbackup
Version  : 1.1.10
Release  : 33
URL      : https://github.com/borgbackup/borg/releases/download/1.1.10/borgbackup-1.1.10.tar.gz
Source0  : https://github.com/borgbackup/borg/releases/download/1.1.10/borgbackup-1.1.10.tar.gz
Source99 : https://github.com/borgbackup/borg/releases/download/1.1.10/borgbackup-1.1.10.tar.gz.asc
Summary  : Deduplicated, encrypted, authenticated and compressed backups
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause CC0-1.0
Requires: borgbackup-bin = %{version}-%{release}
Requires: borgbackup-data = %{version}-%{release}
Requires: borgbackup-license = %{version}-%{release}
Requires: borgbackup-python = %{version}-%{release}
Requires: borgbackup-python3 = %{version}-%{release}
Requires: llfuse
Requires: msgpack-python
BuildRequires : acl-dev
BuildRequires : buildreq-distutils3
BuildRequires : llfuse
BuildRequires : lz4-dev
BuildRequires : openssl-dev
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python3-dev
BuildRequires : setuptools_scm
BuildRequires : tox
BuildRequires : virtualenv
BuildRequires : zstd-dev
Patch1: 0001-Work-around-Borg-self-test-failing.patch

%description
What is BorgBackup?
        -------------------

%package bin
Summary: bin components for the borgbackup package.
Group: Binaries
Requires: borgbackup-data = %{version}-%{release}
Requires: borgbackup-license = %{version}-%{release}

%description bin
bin components for the borgbackup package.


%package data
Summary: data components for the borgbackup package.
Group: Data

%description data
data components for the borgbackup package.


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
%setup -q -n borgbackup-1.1.10
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1561444681
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/borgbackup
cp LICENSE %{buildroot}/usr/share/package-licenses/borgbackup/LICENSE
cp docs/3rd_party/blake2/COPYING %{buildroot}/usr/share/package-licenses/borgbackup/docs_3rd_party_blake2_COPYING
cp docs/3rd_party/lz4/LICENSE %{buildroot}/usr/share/package-licenses/borgbackup/docs_3rd_party_lz4_LICENSE
cp docs/3rd_party/msgpack/COPYING %{buildroot}/usr/share/package-licenses/borgbackup/docs_3rd_party_msgpack_COPYING
cp docs/3rd_party/zstd/LICENSE %{buildroot}/usr/share/package-licenses/borgbackup/docs_3rd_party_zstd_LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
mkdir -p %{buildroot}/usr/share/bash-completion/completions/
install -m 0644 scripts/shell_completions/bash/borg %{buildroot}/usr/share/bash-completion/completions/borg
mkdir -p %{buildroot}/usr/share/fish/completions
install -m 0644 scripts/shell_completions/fish/borg.fish %{buildroot}/usr/share/fish/completions/borg.fish
mkdir -p %{buildroot}/usr/share/zsh/site-functions
install -m 0644 scripts/shell_completions/zsh/_borg %{buildroot}/usr/share/zsh/site-functions/_borg
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/borg
/usr/bin/borgfs

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/borg
/usr/share/fish/completions/borg.fish
/usr/share/zsh/site-functions/_borg

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/borgbackup/LICENSE
/usr/share/package-licenses/borgbackup/docs_3rd_party_blake2_COPYING
/usr/share/package-licenses/borgbackup/docs_3rd_party_lz4_LICENSE
/usr/share/package-licenses/borgbackup/docs_3rd_party_msgpack_COPYING
/usr/share/package-licenses/borgbackup/docs_3rd_party_zstd_LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
