#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v20
# autospec commit: 4ea76c9
#
# Source0 file verified with key 0x243ACFA951F78E01 (tw-public@gmx.de)
#
Name     : borgbackup
Version  : 1.4.0
Release  : 80
URL      : https://github.com/borgbackup/borg/releases/download/1.4.0/borgbackup-1.4.0.tar.gz
Source0  : https://github.com/borgbackup/borg/releases/download/1.4.0/borgbackup-1.4.0.tar.gz
Source1  : https://github.com/borgbackup/borg/releases/download/1.4.0/borgbackup-1.4.0.tar.gz.asc
Source2  : 243ACFA951F78E01.pkey
Summary  : Deduplicated, encrypted, authenticated and compressed backups
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause
Requires: borgbackup-bin = %{version}-%{release}
Requires: borgbackup-data = %{version}-%{release}
Requires: borgbackup-license = %{version}-%{release}
Requires: borgbackup-python = %{version}-%{release}
Requires: borgbackup-python3 = %{version}-%{release}
Requires: pypi(llfuse)
Requires: pypi(msgpack)
BuildRequires : acl-dev
BuildRequires : buildreq-distutils3
BuildRequires : gnupg
BuildRequires : lz4-dev
BuildRequires : openssl-dev
BuildRequires : pypi(cython)
BuildRequires : pypi(pkgconfig)
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(wheel)
BuildRequires : pypi-cython
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
BuildRequires : xxHash-dev
BuildRequires : zstd-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 243ACFA951F78E01' gpg.status
%setup -q -n borgbackup-1.4.0
cd %{_builddir}/borgbackup-1.4.0
pushd ..
cp -a borgbackup-1.4.0 buildavx2
popd

%build
## build_prepend content
rm $(grep -rl '/\* Generated by Cython')
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1730137497
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
## build_prepend content
rm $(grep -rl '/\* Generated by Cython')
## build_prepend end
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/borgbackup
cp %{_builddir}/borgbackup-%{version}/docs/3rd_party/lz4/LICENSE %{buildroot}/usr/share/package-licenses/borgbackup/10bf56381baaf07f0647b93a810eb4e7e9545e8d || :
cp %{_builddir}/borgbackup-%{version}/docs/3rd_party/zstd/LICENSE %{buildroot}/usr/share/package-licenses/borgbackup/c4130945ca3d1f8ea4a3e8af36d3c18b2232116c || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/borgbackup/10bf56381baaf07f0647b93a810eb4e7e9545e8d
/usr/share/package-licenses/borgbackup/c4130945ca3d1f8ea4a3e8af36d3c18b2232116c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
