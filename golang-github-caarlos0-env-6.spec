# Generated by go2rpm 1.6.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/caarlos0/env
%global goipath         github.com/caarlos0/env/v6
Version:                6.9.1

%gometa

%global common_description %{expand:
A simple and zero-dependencies library to parse environment variables into
structs.}

%global golicenses      LICENSE.md
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        A simple and zero-dependencies library to parse environment variables into structs

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
