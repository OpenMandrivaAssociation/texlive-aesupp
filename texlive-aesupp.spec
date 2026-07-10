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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides special support for the italic 'ae' character in
some fonts, due to design flaws (in the author's opinion) regarding this
character. At the moment only the fonts TeX Gyre Bonum, TeX Gyre Schola,
TeX Gyre Pagella, and the Latin Modern fonts are supported. The other
fonts in the TeX Gyre bundle do not need this support.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/fonts
%dir %{_datadir}/texmf-dist/fonts/enc
%dir %{_datadir}/texmf-dist/fonts/map
%dir %{_datadir}/texmf-dist/fonts/opentype
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/fonts/type1
%dir %{_datadir}/texmf-dist/source/fonts
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/fonts/aesupp
%dir %{_datadir}/texmf-dist/fonts/enc/dvips
%dir %{_datadir}/texmf-dist/fonts/map/dvips
%dir %{_datadir}/texmf-dist/fonts/opentype/public
%dir %{_datadir}/texmf-dist/fonts/tfm/public
%dir %{_datadir}/texmf-dist/fonts/type1/public
%dir %{_datadir}/texmf-dist/source/fonts/aesupp
%dir %{_datadir}/texmf-dist/tex/latex/aesupp
%dir %{_datadir}/texmf-dist/fonts/enc/dvips/aesupp
%dir %{_datadir}/texmf-dist/fonts/map/dvips/aesupp
%dir %{_datadir}/texmf-dist/fonts/opentype/public/aesupp
%dir %{_datadir}/texmf-dist/fonts/tfm/public/aesupp
%dir %{_datadir}/texmf-dist/fonts/type1/public/aesupp
%doc %{_datadir}/texmf-dist/doc/fonts/aesupp/GUST-FONT-LICENSE.txt
%doc %{_datadir}/texmf-dist/doc/fonts/aesupp/README
%doc %{_datadir}/texmf-dist/doc/fonts/aesupp/aesupp.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/aesupp/aesupp.tex
%doc %{_datadir}/texmf-dist/doc/fonts/aesupp/ec-aebkbi.pl
%doc %{_datadir}/texmf-dist/doc/fonts/aesupp/ec-aebkri.pl
%doc %{_datadir}/texmf-dist/doc/fonts/aesupp/ec-aecsbi.pl
%doc %{_datadir}/texmf-dist/doc/fonts/aesupp/ec-aecsri.pl
%doc %{_datadir}/texmf-dist/doc/fonts/aesupp/ec-aembxi10.pl
%doc %{_datadir}/texmf-dist/doc/fonts/aesupp/ec-aemri10.pl
%doc %{_datadir}/texmf-dist/doc/fonts/aesupp/ec-aemri12.pl
%doc %{_datadir}/texmf-dist/doc/fonts/aesupp/ec-aemri7.pl
%doc %{_datadir}/texmf-dist/doc/fonts/aesupp/ec-aemri8.pl
%doc %{_datadir}/texmf-dist/doc/fonts/aesupp/ec-aemri9.pl
%doc %{_datadir}/texmf-dist/doc/fonts/aesupp/ec-aemtti10.pl
%doc %{_datadir}/texmf-dist/doc/fonts/aesupp/ec-aeplbi.pl
%doc %{_datadir}/texmf-dist/doc/fonts/aesupp/ec-aeplri.pl
%doc %{_datadir}/texmf-dist/doc/fonts/aesupp/genfonts.pe
%doc %{_datadir}/texmf-dist/doc/fonts/aesupp/ggen.pl
%doc %{_datadir}/texmf-dist/doc/fonts/aesupp/gpl-3.0.txt
%doc %{_datadir}/texmf-dist/doc/fonts/aesupp/rm-aebkbi.pl
%doc %{_datadir}/texmf-dist/doc/fonts/aesupp/rm-aebkri.pl
%doc %{_datadir}/texmf-dist/doc/fonts/aesupp/rm-aecsbi.pl
%doc %{_datadir}/texmf-dist/doc/fonts/aesupp/rm-aecsri.pl
%doc %{_datadir}/texmf-dist/doc/fonts/aesupp/rm-aembxi10.pl
%doc %{_datadir}/texmf-dist/doc/fonts/aesupp/rm-aemri10.pl
%doc %{_datadir}/texmf-dist/doc/fonts/aesupp/rm-aemri12.pl
%doc %{_datadir}/texmf-dist/doc/fonts/aesupp/rm-aemri7.pl
%doc %{_datadir}/texmf-dist/doc/fonts/aesupp/rm-aemri8.pl
%doc %{_datadir}/texmf-dist/doc/fonts/aesupp/rm-aemri9.pl
%doc %{_datadir}/texmf-dist/doc/fonts/aesupp/rm-aemtti10.pl
%doc %{_datadir}/texmf-dist/doc/fonts/aesupp/rm-aeplbi.pl
%doc %{_datadir}/texmf-dist/doc/fonts/aesupp/rm-aeplri.pl
%{_datadir}/texmf-dist/fonts/enc/dvips/aesupp/tg.enc
%{_datadir}/texmf-dist/fonts/map/dvips/aesupp/aesupp.map
%{_datadir}/texmf-dist/fonts/opentype/public/aesupp/aebonum-bolditalic.otf
%{_datadir}/texmf-dist/fonts/opentype/public/aesupp/aebonum-italic.otf
%{_datadir}/texmf-dist/fonts/opentype/public/aesupp/aemmono10-italic.otf
%{_datadir}/texmf-dist/fonts/opentype/public/aesupp/aemroman10-bolditalic.otf
%{_datadir}/texmf-dist/fonts/opentype/public/aesupp/aemroman10-italic.otf
%{_datadir}/texmf-dist/fonts/opentype/public/aesupp/aemroman12-italic.otf
%{_datadir}/texmf-dist/fonts/opentype/public/aesupp/aemroman7-italic.otf
%{_datadir}/texmf-dist/fonts/opentype/public/aesupp/aemroman8-italic.otf
%{_datadir}/texmf-dist/fonts/opentype/public/aesupp/aemroman9-italic.otf
%{_datadir}/texmf-dist/fonts/opentype/public/aesupp/aepagella-bolditalic.otf
%{_datadir}/texmf-dist/fonts/opentype/public/aesupp/aepagella-italic.otf
%{_datadir}/texmf-dist/fonts/opentype/public/aesupp/aeschola-bolditalic.otf
%{_datadir}/texmf-dist/fonts/opentype/public/aesupp/aeschola-italic.otf
%{_datadir}/texmf-dist/fonts/tfm/public/aesupp/aebkbi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aesupp/aebkri.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aesupp/aecsbi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aesupp/aecsri.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aesupp/aembxi10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aesupp/aemri10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aesupp/aemri12.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aesupp/aemri7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aesupp/aemri8.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aesupp/aemri9.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aesupp/aemtti10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aesupp/aeplbi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aesupp/aeplri.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aesupp/ec-aebkbi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aesupp/ec-aebkri.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aesupp/ec-aecsbi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aesupp/ec-aecsri.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aesupp/ec-aembxi10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aesupp/ec-aemri10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aesupp/ec-aemri12.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aesupp/ec-aemri7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aesupp/ec-aemri8.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aesupp/ec-aemri9.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aesupp/ec-aemtti10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aesupp/ec-aeplbi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aesupp/ec-aeplri.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aesupp/rm-aebkbi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aesupp/rm-aebkri.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aesupp/rm-aecsbi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aesupp/rm-aecsri.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aesupp/rm-aembxi10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aesupp/rm-aemri10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aesupp/rm-aemri12.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aesupp/rm-aemri7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aesupp/rm-aemri8.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aesupp/rm-aemri9.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aesupp/rm-aemtti10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aesupp/rm-aeplbi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/aesupp/rm-aeplri.tfm
%{_datadir}/texmf-dist/fonts/type1/public/aesupp/aebkbi.pfb
%{_datadir}/texmf-dist/fonts/type1/public/aesupp/aebkri.pfb
%{_datadir}/texmf-dist/fonts/type1/public/aesupp/aecsbi.pfb
%{_datadir}/texmf-dist/fonts/type1/public/aesupp/aecsri.pfb
%{_datadir}/texmf-dist/fonts/type1/public/aesupp/aembxi10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/aesupp/aemri10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/aesupp/aemri12.pfb
%{_datadir}/texmf-dist/fonts/type1/public/aesupp/aemri7.pfb
%{_datadir}/texmf-dist/fonts/type1/public/aesupp/aemri8.pfb
%{_datadir}/texmf-dist/fonts/type1/public/aesupp/aemri9.pfb
%{_datadir}/texmf-dist/fonts/type1/public/aesupp/aemtti10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/aesupp/aeplbi.pfb
%{_datadir}/texmf-dist/fonts/type1/public/aesupp/aeplri.pfb
%doc %{_datadir}/texmf-dist/source/fonts/aesupp/aebonum-bolditalic.sfd
%doc %{_datadir}/texmf-dist/source/fonts/aesupp/aebonum-italic.sfd
%doc %{_datadir}/texmf-dist/source/fonts/aesupp/aemmono10-italic.sfd
%doc %{_datadir}/texmf-dist/source/fonts/aesupp/aemroman10-bolditalic.sfd
%doc %{_datadir}/texmf-dist/source/fonts/aesupp/aemroman10-italic.sfd
%doc %{_datadir}/texmf-dist/source/fonts/aesupp/aemroman12-italic.sfd
%doc %{_datadir}/texmf-dist/source/fonts/aesupp/aemroman7-italic.sfd
%doc %{_datadir}/texmf-dist/source/fonts/aesupp/aemroman8-italic.sfd
%doc %{_datadir}/texmf-dist/source/fonts/aesupp/aemroman9-italic.sfd
%doc %{_datadir}/texmf-dist/source/fonts/aesupp/aepagella-bolditalic.sfd
%doc %{_datadir}/texmf-dist/source/fonts/aesupp/aepagella-italic.sfd
%doc %{_datadir}/texmf-dist/source/fonts/aesupp/aeschola-bolditalic.sfd
%doc %{_datadir}/texmf-dist/source/fonts/aesupp/aeschola-italic.sfd
%{_datadir}/texmf-dist/tex/latex/aesupp/aesupp.sty
