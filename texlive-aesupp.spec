Name:		texlive-aesupp
Version:	58253
Release:	2
Summary:	Special support for the ae character
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/aesupp
License:	gfl gpl3+
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aesupp.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aesupp.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aesupp.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides special support for the italic 'ae'
character in some fonts, due to design flaws (in the author's
opinion) regarding this character. At the moment only the fonts
TeX Gyre Bonum, TeX Gyre Schola, TeX Gyre Pagella, and the
Latin Modern fonts are supported. The other fonts in the TeX
Gyre bundle do not need this support.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/fonts/aesupp
%{_texmfdistdir}/tex/latex/aesupp
%{_texmfdistdir}/fonts/type1/public/aesupp
%{_texmfdistdir}/fonts/tfm/public/aesupp
%{_texmfdistdir}/fonts/opentype/public/aesupp
%{_texmfdistdir}/fonts/map/dvips/aesupp
%{_texmfdistdir}/fonts/enc/dvips/aesupp
%doc %{_texmfdistdir}/doc/fonts/aesupp

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
