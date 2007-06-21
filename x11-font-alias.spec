Name: x11-font-alias
Version: 1.0.1
Release: %mkrel 8
Summary: Xorg X11 font alias
Group: Development/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/font/font-alias-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root
BuildArch: noarch
Conflicts: xorg-x11 < 7.0

Requires(post): mkfontdir
Requires(post): mkfontscale

BuildRequires: x11-util-macros >= 1.0.1

%description
Xorg X11 font aliases

%prep
%setup -q -n font-alias-%{version}

%build
%configure2_5x --with-top-fontdir=%_datadir/fonts

%make

%install
rm -rf %{buildroot}
%makeinstall_std

# create empty ghost files
for dir in 100dpi 75dpi cyrillic misc OTF Speedo TTF Type1; do
	mkdir -p %{buildroot}%_datadir/fonts/$dir
	touch %{buildroot}%_datadir/fonts/$dir/fonts.{dir,scale}
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


