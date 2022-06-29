#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-ellipsis
Version  : 0.3.2
Release  : 37
URL      : https://cran.r-project.org/src/contrib/ellipsis_0.3.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ellipsis_0.3.2.tar.gz
Summary  : Tools for Working with ...
Group    : Development/Tools
License  : MIT
Requires: R-ellipsis-lib = %{version}-%{release}
Requires: R-rlang
BuildRequires : R-rlang
BuildRequires : buildreq-R

%description
# ellipsis
<!-- badges: start -->
[![Lifecycle:
maturing](https://img.shields.io/badge/lifecycle-maturing-blue.svg)](https://lifecycle.r-lib.org/articles/stages.html)
[![CRAN
status](https://www.r-pkg.org/badges/version/ellipsis)](https://cran.r-project.org/package=ellipsis)
[![Travis build
status](https://travis-ci.org/r-lib/ellipsis.svg?branch=master)](https://travis-ci.org/r-lib/ellipsis)
[![Codecov test
coverage](https://codecov.io/gh/r-lib/ellipsis/branch/master/graph/badge.svg)](https://codecov.io/gh/r-lib/ellipsis?branch=master)
<!-- badges: end -->

%package lib
Summary: lib components for the R-ellipsis package.
Group: Libraries

%description lib
lib components for the R-ellipsis package.


%prep
%setup -q -c -n ellipsis
cd %{_builddir}/ellipsis

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641007176

%install
export SOURCE_DATE_EPOCH=1641007176
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ellipsis
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ellipsis
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ellipsis
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc ellipsis || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ellipsis/DESCRIPTION
/usr/lib64/R/library/ellipsis/INDEX
/usr/lib64/R/library/ellipsis/LICENSE
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
/usr/lib64/R/library/ellipsis/libs/ellipsis.so.avx2
/usr/lib64/R/library/ellipsis/libs/ellipsis.so.avx512
