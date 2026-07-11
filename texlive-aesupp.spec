%global tl_name aesupp
%global tl_revision 58253

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1
Release:	%{tl_revision}.1
Summary:	Special support for the ae character
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/aesupp
License:	gfl gpl3+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aesupp.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aesupp.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aesupp.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides special support for the italic 'ae' character in
some fonts, due to design flaws (in the author's opinion) regarding this
character. At the moment only the fonts TeX Gyre Bonum, TeX Gyre Schola,
TeX Gyre Pagella, and the Latin Modern fonts are supported. The other
fonts in the TeX Gyre bundle do not need this support.

