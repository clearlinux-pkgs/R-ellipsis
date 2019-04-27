#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-ellipsis
Version  : 0.1.0
Release  : 8
URL      : https://cran.r-project.org/src/contrib/ellipsis_0.1.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ellipsis_0.1.0.tar.gz
Summary  : Tools for Working with ...
Group    : Development/Tools
License  : GPL-3.0
Requires: R-ellipsis-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
# ellipsis
[![lifecycle](https://img.shields.io/badge/lifecycle-experimental-orange.svg)](https://www.tidyverse.org/lifecycle/#experimental)
[![Travis build
status](https://travis-ci.org/hadley/ellipsis.svg?branch=master)](https://travis-ci.org/hadley/ellipsis)
[![Coverage
status](https://codecov.io/gh/hadley/ellipsis/branch/master/graph/badge.svg)](https://codecov.io/github/hadley/ellipsis?branch=master)

%package lib
Summary: lib components for the R-ellipsis package.
Group: Libraries

%description lib
lib components for the R-ellipsis package.


%prep
%setup -q -c -n ellipsis

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552920470

%install
export SOURCE_DATE_EPOCH=1552920470
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ellipsis
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ellipsis
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ellipsis
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  ellipsis || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ellipsis/DESCRIPTION
/usr/lib64/R/library/ellipsis/INDEX
/usr/lib64/R/library/ellipsis/Meta/Rd.rds
/usr/lib64/R/library/ellipsis/Meta/features.rds
/usr/lib64/R/library/ellipsis/Meta/hsearch.rds
/usr/lib64/R/library/ellipsis/Meta/links.rds
/usr/lib64/R/library/ellipsis/Meta/nsInfo.rds
/usr/lib64/R/library/ellipsis/Meta/package.rds
/usr/lib64/R/library/ellipsis/NAMESPACE
/usr/lib64/R/library/ellipsis/NEWS.md
/usr/lib64/R/library/ellipsis/R/ellipsis
/usr/lib64/R/library/ellipsis/R/ellipsis.rdb
/usr/lib64/R/library/ellipsis/R/ellipsis.rdx
/usr/lib64/R/library/ellipsis/help/AnIndex
/usr/lib64/R/library/ellipsis/help/aliases.rds
/usr/lib64/R/library/ellipsis/help/ellipsis.rdb
/usr/lib64/R/library/ellipsis/help/ellipsis.rdx
/usr/lib64/R/library/ellipsis/help/paths.rds
/usr/lib64/R/library/ellipsis/html/00Index.html
/usr/lib64/R/library/ellipsis/html/R.css
/usr/lib64/R/library/ellipsis/tests/testthat.R
/usr/lib64/R/library/ellipsis/tests/testthat/test-check.R
/usr/lib64/R/library/ellipsis/tests/testthat/test-dots.R
/usr/lib64/R/library/ellipsis/tests/testthat/test-safe.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/ellipsis/libs/ellipsis.so
