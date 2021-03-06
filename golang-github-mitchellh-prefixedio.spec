# Generated by go2rpm 1.6.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/mitchellh/prefixedio
%global goipath         github.com/mitchellh/prefixedio
%global commit          5733675afd5162de652b410d2244d82b00a38a79

%gometa

%global common_description %{expand:
Golang library that demultiplexes line-oriented data from an io.Reader into
multiple io.Readers based on a prefix.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        %autorelease -p
Summary:        Golang library that demultiplexes line-oriented data from an io.Reader into multiple io.Readers based on a prefix

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
