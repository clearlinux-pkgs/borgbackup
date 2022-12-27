#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x243ACFA951F78E01 (tw-public@gmx.de)
#
Name     : borgbackup
Version  : 1.2.3
Release  : 65
URL      : https://github.com/borgbackup/borg/releases/download/1.2.3/borgbackup-1.2.3.tar.gz
Source0  : https://github.com/borgbackup/borg/releases/download/1.2.3/borgbackup-1.2.3.tar.gz
Source1  : https://github.com/borgbackup/borg/releases/download/1.2.3/borgbackup-1.2.3.tar.gz.asc
Summary  : Deduplicated, encrypted, authenticated and compressed backups
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause
Requires: borgbackup-bin = %{version}-%{release}
Requires: borgbackup-data = %{version}-%{release}
Requires: borgbackup-filemap = %{version}-%{release}
Requires: borgbackup-lib = %{version}-%{release}
Requires: borgbackup-license = %{version}-%{release}
Requires: borgbackup-python = %{version}-%{release}
Requires: borgbackup-python3 = %{version}-%{release}
Requires: pypi(llfuse)
Requires: pypi(msgpack)
BuildRequires : acl-dev
BuildRequires : buildreq-distutils3
BuildRequires : lz4-dev
BuildRequires : openssl-dev
BuildRequires : pypi(cython)
BuildRequires : pypi(msgpack)
BuildRequires : pypi(packaging)
BuildRequires : pypi(pkgconfig)
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi-cython
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
BuildRequires : zstd-dev

%description
Do NOT run the examples without isolation (e.g Vagrant) or
this code may make undesirable changes to your host.

%package bin
Summary: bin components for the borgbackup package.
Group: Binaries
Requires: borgbackup-data = %{version}-%{release}
Requires: borgbackup-license = %{version}-%{release}
Requires: borgbackup-filemap = %{version}-%{release}

%description bin
bin components for the borgbackup package.


%package data
Summary: data components for the borgbackup package.
Group: Data

%description data
data components for the borgbackup package.


%package filemap
Summary: filemap components for the borgbackup package.
Group: Default

%description filemap
filemap components for the borgbackup package.


%package lib
Summary: lib components for the borgbackup package.
Group: Libraries
Requires: borgbackup-data = %{version}-%{release}
Requires: borgbackup-license = %{version}-%{release}
Requires: borgbackup-filemap = %{version}-%{release}

%description lib
lib components for the borgbackup package.


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
Requires: borgbackup-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(borgbackup)
Requires: pypi(msgpack)
Requires: pypi(packaging)

%description python3
python3 components for the borgbackup package.


%prep
%setup -q -n borgbackup-1.2.3
cd %{_builddir}/borgbackup-1.2.3
pushd ..
cp -a borgbackup-1.2.3 buildavx2
cp -a borgbackup-1.2.3 buildavx512
popd

%build
## build_prepend content
rm $(grep -rl '/\* Generated by Cython')
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672165727
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
## build_prepend content
rm $(grep -rl '/\* Generated by Cython')
## build_prepend end
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/borgbackup
cp %{_builddir}/borgbackup-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/borgbackup/0743da544cad745983ac9011cc39e7d6b6933fa3
cp %{_builddir}/borgbackup-%{version}/docs/3rd_party/lz4/LICENSE %{buildroot}/usr/share/package-licenses/borgbackup/10bf56381baaf07f0647b93a810eb4e7e9545e8d
cp %{_builddir}/borgbackup-%{version}/docs/3rd_party/zstd/LICENSE %{buildroot}/usr/share/package-licenses/borgbackup/c4130945ca3d1f8ea4a3e8af36d3c18b2232116c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
## install_append content
# Install shell completion support
mkdir -p %{buildroot}/usr/share/bash-completion/completions/
install -m 0644 scripts/shell_completions/bash/borg %{buildroot}/usr/share/bash-completion/completions/borg
mkdir -p %{buildroot}/usr/share/fish/completions
install -m 0644 scripts/shell_completions/fish/borg.fish %{buildroot}/usr/share/fish/completions/borg.fish
mkdir -p %{buildroot}/usr/share/zsh/site-functions
install -m 0644 scripts/shell_completions/zsh/_borg %{buildroot}/usr/share/zsh/site-functions/_borg
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-borgbackup

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/borgbackup/0743da544cad745983ac9011cc39e7d6b6933fa3
/usr/share/package-licenses/borgbackup/10bf56381baaf07f0647b93a810eb4e7e9545e8d
/usr/share/package-licenses/borgbackup/c4130945ca3d1f8ea4a3e8af36d3c18b2232116c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
