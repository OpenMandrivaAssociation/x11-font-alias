Name: x11-font-alias
Version: 1.0.3
Release: 9
Summary: Xorg X11 font alias
Group: Development/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/font/font-alias-%{version}.tar.bz2
License: MIT-like
BuildRoot: %{_tmppath}/%{name}-root
BuildArch: noarch
Conflicts: xorg-x11 < 7.0

# fonts/misc dir was moved to this package
Conflicts: x11-font-misc-misc < 1.0.0-6mdv

Requires(post): mkfontdir
Requires(post): mkfontscale

BuildRequires: x11-util-macros >= 1.0.1

%description
Xorg X11 font aliases

%prep
%setup -q -n font-alias-%{version}

%build
./configure --prefix=/usr --with-fontrootdir=%_datadir/fonts

%make

%install
rm -rf %{buildroot}
%makeinstall_std

# create empty ghost files
for dir in 100dpi 75dpi cyrillic misc OTF Speedo TTF Type1; do
	mkdir -p %{buildroot}%_datadir/fonts/$dir
	touch %{buildroot}%_datadir/fonts/$dir/fonts.{dir,scale}
done

# fontpath.d symlinks
mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/misc \
	%{buildroot}%_sysconfdir/X11/fontpath.d/misc:unscaled:pri=10
ln -s ../../..%_datadir/fonts/75dpi \
	%{buildroot}%_sysconfdir/X11/fontpath.d/75dpi:unscaled:pri=20
ln -s ../../..%_datadir/fonts/100dpi \
	%{buildroot}%_sysconfdir/X11/fontpath.d/100dpi:unscaled:pri=30
for dir in cyrillic OTF Speedo TTF Type1; do
	ln -s ../../..%_datadir/fonts/$dir \
		%{buildroot}%_sysconfdir/X11/fontpath.d/$dir:pri=40
done

%clean
rm -rf %{buildroot}

%post
for dir in 100dpi 75dpi cyrillic misc OTF Speedo TTF Type1; do
    cd %_datadir/fonts/$dir
    mkfontscale
    mkfontdir
done

%files
%defattr(-,root,root)
%dir %_datadir/fonts/misc
%dir %_datadir/fonts/100dpi
%dir %_datadir/fonts/75dpi
%dir %_datadir/fonts/cyrillic
%dir %_datadir/fonts/OTF
%dir %_datadir/fonts/Speedo
%dir %_datadir/fonts/TTF
%dir %_datadir/fonts/Type1

# XXX: this may be fragmented inside individual
# x11 fontpackages, but it's OK by now
%_sysconfdir/X11/fontpath.d/misc:unscaled:pri=10
%_sysconfdir/X11/fontpath.d/75dpi:unscaled:pri=20
%_sysconfdir/X11/fontpath.d/100dpi:unscaled:pri=30
%_sysconfdir/X11/fontpath.d/cyrillic:pri=40
%_sysconfdir/X11/fontpath.d/OTF:pri=40
%_sysconfdir/X11/fontpath.d/Speedo:pri=40
%_sysconfdir/X11/fontpath.d/TTF:pri=40
%_sysconfdir/X11/fontpath.d/Type1:pri=40

%_datadir/fonts/100dpi/fonts.alias
%_datadir/fonts/75dpi/fonts.alias
%_datadir/fonts/cyrillic/fonts.alias
%_datadir/fonts/misc/fonts.alias

# fonts.dir and fonts.scale files
%_datadir/fonts/100dpi/fonts.dir
%_datadir/fonts/100dpi/fonts.scale
%_datadir/fonts/75dpi/fonts.dir
%_datadir/fonts/75dpi/fonts.scale
%_datadir/fonts/cyrillic/fonts.dir
%_datadir/fonts/cyrillic/fonts.scale
%_datadir/fonts/misc/fonts.dir
%_datadir/fonts/misc/fonts.scale
%_datadir/fonts/OTF/fonts.dir
%_datadir/fonts/OTF/fonts.scale
%_datadir/fonts/Speedo/fonts.dir
%_datadir/fonts/Speedo/fonts.scale
%_datadir/fonts/TTF/fonts.dir
%_datadir/fonts/TTF/fonts.scale
%_datadir/fonts/Type1/fonts.dir
%_datadir/fonts/Type1/fonts.scale



%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.0.3-3mdv2011.0
+ Revision: 675196
- rebuild for new rpm-setup

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-2
+ Revision: 671191
- mass rebuild

* Wed Oct 06 2010 Thierry Vignaud <tv@mandriva.org> 1.0.3-1mdv2011.0
+ Revision: 583166
- new release

* Thu Jan 14 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.2-1mdv2010.1
+ Revision: 491251
- Upstream compiled a COPYING file with a MIT-like license (current one says we
  should check each file's license)
- New version: 1.0.2

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.1-14mdv2009.1
+ Revision: 351364
- rebuild

* Fri Jun 20 2008 Pixel <pixel@mandriva.com> 1.0.1-13mdv2009.0
+ Revision: 227381
- move back from %%{_datadir}/X11/fontpath.d to %%{_sysconfdir}/X11/fontpath.d until changed again in x11-server

* Wed May 14 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.1-12mdv2009.0
+ Revision: 207241
- Move symlinks from %%{_sysconfdir}/X11/fontpath.d to
  %%{_datadir}/X11/fontpath.d.

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-12mdv2008.1
+ Revision: 179656
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Jul 06 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.0.1-11mdv2008.0
+ Revision: 49185
- cosmetic: remove extra / from font-path symlinks

* Thu Jul 05 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.0.1-10mdv2008.0
+ Revision: 48677
- x11-font-misc-misc was fixed, so we can add the
  dir fonts/misc to this package.

* Thu Jul 05 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.0.1-9mdv2008.0
+ Revision: 48626
- add font directories to %%files (they were orphans)
- add fontpath.d support for standard fonts (see #31756)
  (maybe it's a good idea to merge this package inside
  x11-server-common or rename it, but it's OK by now)


* Thu Aug 03 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-08-03 18:39:34 (51422)
- All fonts now moved to /usr/share/fonts. font-alias need point to correct place

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Tue May 23 2006 Pixel <pixel@mandriva.com>
+ 2006-05-23 09:58:02 (27879)
- mkfontdir uses fonts.scale, so mkfontscale must be done before mkfontdir
  (forget the previous buggy commit log...)

* Tue May 23 2006 Pixel <pixel@mandriva.com>
+ 2006-05-23 09:55:39 (27878)
- use Requires(post) instead of PreReq

* Mon May 22 2006 Pixel <pixel@mandriva.com>
+ 2006-05-22 13:43:08 (27844)
- use Requires(post) instead of PreReq

* Mon May 22 2006 Pixel <pixel@mandriva.com>
+ 2006-05-22 13:38:11 (27843)
- fix typo (fonts.dir were not being built, so were empty)

* Thu May 18 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-18 20:14:29 (27644)
- 3mdk

* Thu May 18 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-18 15:08:18 (27612)
- Add fonts.{dir,scale} to this package just for the upgrade process to be smooth

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

