Summary:	Tomboy is a desktop note-taking application
Name:		tomboy
Version:	0.2.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.beatniksoftware.com/tomboy/releases/%{name}-%{version}.tar.gz
# Source0-md5:	be87c798d7f978c307433485cbd38f4e
Patch0:		%{name}-desktop.patch
URL:		http://www.beatniksoftware.com/tomboy/
BuildRequires:	GConf2-devel
BuildRequires:	atk-devel >= 1.2.4
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-dbus-sharp-devel
BuildRequires:	dotnet-gtk-sharp-devel
BuildRequires:	gtkspell-devel >= 2.0.5
BuildRequires:	intltool >= 0.25
BuildRequires:	libtool
BuildRequires:	mono-csharp
BuildRequires:	pkgconfig
Requires(post):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tomboy is a desktop note-taking application for Linux and Unix. Simple
and easy to use, but with potential to help you organize the ideas and
information you deal with every day.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/*.schemas
%{_libdir}/dbus-1.0/services/*.service
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*.so
%attr(755,root,root) %{_libdir}/%{name}/*.exe
%{_libdir}/%{name}/*.dll
%{_desktopdir}/*.desktop
%{_mandir}/man1/tomboy.1*
%{_pixmapsdir}/*.png
