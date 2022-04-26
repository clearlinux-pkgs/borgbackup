#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x243ACFA951F78E01 (tw-public@gmx.de)
#
Name     : borgbackup
Version  : 1.1.17
Release  : 59
URL      : https://github.com/borgbackup/borg/releases/download/1.1.17/borgbackup-1.1.17.tar.gz
Source0  : https://github.com/borgbackup/borg/releases/download/1.1.17/borgbackup-1.1.17.tar.gz
Source1  : https://github.com/borgbackup/borg/releases/download/1.1.17/borgbackup-1.1.17.tar.gz.asc
Summary  : Deduplicated, encrypted, authenticated and compressed backups
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause CC0-1.0
Requires: borgbackup-bin = %{version}-%{release}
Requires: borgbackup-data = %{version}-%{release}
Requires: borgbackup-license = %{version}-%{release}
Requires: borgbackup-python = %{version}-%{release}
Requires: borgbackup-python3 = %{version}-%{release}
Requires: pypi(llfuse)
Requires: pypi(msgpack)
BuildRequires : acl-dev
BuildRequires : buildreq-distutils3
BuildRequires : lz4-dev
BuildRequires : openssl-dev
BuildRequires : pypi(packaging)
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
BuildRequires : python3-dev
BuildRequires : zstd-dev

%description
Here we store 3rd party documentation, licenses, etc.
Please note that all files inside the "borg" package directory (except the
stuff excluded in setup.py) will be INSTALLED, so don't keep docs or licenses
there.

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
Provides: pypi(borgbackup)
Requires: pypi(packaging)

%description python3
python3 components for the borgbackup package.


%prep
%setup -q -n borgbackup-1.1.17
cd %{_builddir}/borgbackup-1.1.17

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1650932030
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/borgbackup
cp %{_builddir}/borgbackup-1.1.17/LICENSE %{buildroot}/usr/share/package-licenses/borgbackup/87cb76efc3c2fc3582eb2ed5f760f354aefbc43a
cp %{_builddir}/borgbackup-1.1.17/docs/3rd_party/blake2/COPYING %{buildroot}/usr/share/package-licenses/borgbackup/d32fa0b0c2b059b3fd4d2a317d0cf1cd0da791d4
cp %{_builddir}/borgbackup-1.1.17/docs/3rd_party/lz4/LICENSE %{buildroot}/usr/share/package-licenses/borgbackup/10bf56381baaf07f0647b93a810eb4e7e9545e8d
cp %{_builddir}/borgbackup-1.1.17/docs/3rd_party/msgpack/COPYING %{buildroot}/usr/share/package-licenses/borgbackup/175e59be229a5bedc6be93e958a970385bb04a62
cp %{_builddir}/borgbackup-1.1.17/docs/3rd_party/zstd/LICENSE %{buildroot}/usr/share/package-licenses/borgbackup/c4130945ca3d1f8ea4a3e8af36d3c18b2232116c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
# Install shell completion support
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
/usr/share/package-licenses/borgbackup/10bf56381baaf07f0647b93a810eb4e7e9545e8d
/usr/share/package-licenses/borgbackup/175e59be229a5bedc6be93e958a970385bb04a62
/usr/share/package-licenses/borgbackup/87cb76efc3c2fc3582eb2ed5f760f354aefbc43a
/usr/share/package-licenses/borgbackup/c4130945ca3d1f8ea4a3e8af36d3c18b2232116c
/usr/share/package-licenses/borgbackup/d32fa0b0c2b059b3fd4d2a317d0cf1cd0da791d4

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
