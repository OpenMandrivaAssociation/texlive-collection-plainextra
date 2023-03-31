# revision 31683
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-plainextra
Epoch:		1
Version:	20131013
Release:	11
Summary:	Plain TeX packages
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-plainextra.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-basic
Requires:	texlive-figflow
Requires:	texlive-fixpdfmag
Requires:	texlive-font-change
Requires:	texlive-fontch
Requires:	texlive-getoptk
Requires:	texlive-graphics-pln
Requires:	texlive-hyplain
Requires:	texlive-js-misc
Requires:	texlive-mkpattern
Requires:	texlive-newsletr
Requires:	texlive-pitex
Requires:	texlive-placeins-plain
Requires:	texlive-plipsum
Requires:	texlive-plnfss
Requires:	texlive-plstmary
Requires:	texlive-present
Requires:	texlive-resumemac
Requires:	texlive-texinfo
Requires:	texlive-timetable
Requires:	texlive-treetex
Requires:	texlive-varisize
Requires:	texlive-xii

%description
Add-on packages and macros that work with plain TeX.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
