Summary:	Flare is a free ActionScript decompiler.
Name:		flare
Version:	0.5
Release:	2
License:	freeware
Group:		Development
Source0:	http://www.nowrap.de/download/%{name}05linux.tgz
# Source0-md5:	fbcd91d260e0ed6ed6d6fc566e6c5c69
Source1:	%{name}.sh
URL:		http://www.nowrap.de/flare.html
Requires:	mktemp
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Flare processes an SWF and extracts all scripts from it. The output is
written to a single text file. Only ActionScript is extracted, no text
or images.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install flare $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.TXT flare.html classic.css
%attr(755,root,root) %{_bindir}/flare
%attr(755,root,root) %{_bindir}/flare.sh
