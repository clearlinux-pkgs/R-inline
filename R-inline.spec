#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-inline
Version  : 0.3.19
Release  : 55
URL      : https://cran.r-project.org/src/contrib/inline_0.3.19.tar.gz
Source0  : https://cran.r-project.org/src/contrib/inline_0.3.19.tar.gz
Summary  : Functions to Inline C, C++, Fortran Function Calls from R
Group    : Development/Tools
License  : LGPL-2.1
BuildRequires : buildreq-R

%description
with 'inlined' C, C++ or Fortran code supporting the .C and .Call calling
 conventions.

%prep
%setup -q -c -n inline
cd %{_builddir}/inline

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641037421

%install
export SOURCE_DATE_EPOCH=1641037421
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library inline
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library inline
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library inline
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc inline || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/inline/DESCRIPTION
/usr/lib64/R/library/inline/INDEX
/usr/lib64/R/library/inline/Meta/Rd.rds
/usr/lib64/R/library/inline/Meta/features.rds
/usr/lib64/R/library/inline/Meta/hsearch.rds
/usr/lib64/R/library/inline/Meta/links.rds
/usr/lib64/R/library/inline/Meta/nsInfo.rds
/usr/lib64/R/library/inline/Meta/package.rds
/usr/lib64/R/library/inline/NAMESPACE
/usr/lib64/R/library/inline/NEWS.Rd
/usr/lib64/R/library/inline/R/inline
/usr/lib64/R/library/inline/R/inline.rdb
/usr/lib64/R/library/inline/R/inline.rdx
/usr/lib64/R/library/inline/help/AnIndex
/usr/lib64/R/library/inline/help/aliases.rds
/usr/lib64/R/library/inline/help/inline.rdb
/usr/lib64/R/library/inline/help/inline.rdx
/usr/lib64/R/library/inline/help/paths.rds
/usr/lib64/R/library/inline/html/00Index.html
/usr/lib64/R/library/inline/html/R.css
/usr/lib64/R/library/inline/tests/tinytest.R
/usr/lib64/R/library/inline/tinytest/test_cfunction.R
/usr/lib64/R/library/inline/tinytest/test_cxxfunction.R
/usr/lib64/R/library/inline/tinytest/test_utilities.R
