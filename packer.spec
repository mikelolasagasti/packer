# Generated by go2rpm 1.6.0
%bcond_without check

# https://github.com/hashicorp/packer
%global goipath         github.com/hashicorp/packer
Version:                1.7.9

%gometa

%global goname packer

%global common_description %{expand:
Packer is a tool for creating identical machine images for multiple platforms
from a single source configuration.}

%global golicenses      LICENSE website/LICENSE.md post-\\\
                        processor/compress/LICENSE post-\\\
                        processor/checksum/LICENSE
%global godocs          CHANGELOG.md README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Packer is a tool for creating identical machine images for multiple platforms from a single source configuration

# Upstream license specification: MPL-2.0 and MIT
License:        MPLv2.0 and MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%gobuild -o %{gobuilddir}/bin/packer %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE post-processor/compress/LICENSE
%license post-processor/checksum/LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog