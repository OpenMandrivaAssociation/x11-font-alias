Name: x11-font-alias
Version: 1.0.3
Release: %mkrel 3
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

