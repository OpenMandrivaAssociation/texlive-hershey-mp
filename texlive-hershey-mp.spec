Name:		texlive-hershey-mp
Version:	64878
Release:	2
Summary:	MetaPost support for the Hershey font file format
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hershey-mp
License:	other-free
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hershey-mp.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hershey-mp.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides MetaPost support for reading jhf vector
font files, used by (mostly? only?) the so-called Hershey Fonts
of the late 1960s. The package does not include the actual font
files, which you can probably find in the software repository
of your operating system.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/metapost/hershey-mp
%doc %{_texmfdistdir}/doc/metapost/hershey-mp

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
