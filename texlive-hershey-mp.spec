%global tl_name hershey-mp
%global tl_revision 70885

Name:		texlive-%{tl_name}
Epoch:		1
Version:	20221.0
Release:	%{tl_revision}.1
Summary:	MetaPost support for the Hershey font file format
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/hershey-mp
License:	eupl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hershey-mp.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hershey-mp.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides MetaPost support for reading jhf vector font
files, used by (mostly? only?) the so-called Hershey Fonts of the late
1960s. The package does not include the actual font files, which you can
probably find in the software repository of your operating system.

