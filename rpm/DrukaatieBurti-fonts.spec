%define catalogue %{_sysconfdir}/X11/fontpath.d
%global priority  64
%global fontname  DrukaatieBurti

Name:             %{fontname}-fonts
Summary:          Another technical handwriting font.
Version:          0.14.4
Release:          K01%{?dist}
Packager:         Kārlis Kalviškis
License:          SIL OFL
Group:            User Interface/X
URL:              http://priede.bf.lu.lv/ftp/Linux/Fedora/
Source0:          %{fontname}-%{version}.tar.xz
Source1:          %{fontname}.conf
BuildArch:        noarch
BuildRequires:    fontpackages-devel >= 1.13, xorg-x11-font-utils
BuildRequires:    fontforge
Obsoletes:        %{fontname}

%description
The font “DrukaatieBurti” has the same height as „Liberation Serif” 
font. Texts using „Drukaatie burti” (Regular) takes approximately the 
same space as texts using „Liberation Serif Regular”.


%prep
%setup -n  %{fontname}-%{version}

%build
make %{?_smp_mflags} 
mv  %{fontname}-ttf-%{version}/* .


%install
# fonts .ttf
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}
# catalogue
install -m 0755 -d %{buildroot}%{catalogue}
ln -s %{_fontdir} %{buildroot}%{catalogue}/%{fontname}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

%global fconf  %{priority}-%{fontname}.conf
install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fconf}
ln -s %{_fontconfig_templatedir}/%{fconf} \
        %{buildroot}%{_fontconfig_confdir}/%{fconf}

# fonts.{dir,scale}
mkfontscale %{buildroot}%{_fontdir}
mkfontdir %{buildroot}%{_fontdir}

mkdir -p ${RPM_BUILD_ROOT}%{_docdir}/%{fontname}
cp AUTHORS ChangeLog COPYING README TODO ${RPM_BUILD_ROOT}%{_docdir}/%{fontname}

%files
%defattr(-,root,root)
%{_datadir}
# %dir %{_fontdir}
%{catalogue}/%{fontname}
%{_fontconfig_confdir}


%changelog

* Thu Feb 23 2023 Kārlis Kalviškis <karlo at lu.lv> - K01-0.14.4
- The width of Non-breaking space set to the with of ordinary space.
- Some symbols added.

* Wed Feb 05 2020 Kārlis Kalviškis <karlo at lu.lv> - K01-0.14.3
- The name of RPM package is changed.
- Kerning classes has been added.

* Wed Oct 12 2016 Kārlis Kalviškis <eko at lanet.lv>
- The width of plus sign has been corrected.

* Wed Apr 08 2015 Kārlis Kalviškis <eko at lanet.lv>
- For the font “DrukaatieBurti-Regular” the OS/2 Weight Class
  has been changed to “400 Regular”. 

* Sat Mar 28 2015 Kārlis Kalviškis <eko at lanet.lv>
- For compatibilityreasons “DrukaatieBurti-Medium” is
  renamed as “DrukaatieBurti-Regular”.
- The placements of the diacritic marks are emproved.

* Thu Mar 26 2015 Kārlis Kalviškis <eko at lanet.lv>
- Row spacing has been made more compatible with different systems.

* Wed Mar 25 2015 Kārlis Kalviškis <eko@lanet.lv>
- Inital packaging
