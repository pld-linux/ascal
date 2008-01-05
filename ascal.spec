Summary:	GNOME Version of the board game Lasca
Summary(pl.UTF-8):	Wersja gry Lasca dla GNOME
Name:		ascal
Version:	0.1.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/ascal/%{name}-%{version}.tar.bz2
# Source0-md5:	d0121cac9ab3af6b5ef6501fd602b96c
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-optimization.patch
Patch2:		%{name}-gcc.patch
URL:		http://sourceforge.net/projects/ascal/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	libglademm >= 2.4.0
BuildRequires:	libgnomecanvasmm-devel >= 2.0.0
BuildRequires:	libsigc++-devel >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lasca is a game similar to Draughts but with some really cool
enhancements.

%description -l pl.UTF-8
Lasca to gra podobna do warcabów, ale mająca wiele ciekawych
ulepszeń.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__intltoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
