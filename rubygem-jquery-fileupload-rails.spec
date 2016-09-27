# Generated from jquery-fileupload-rails-0.3.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name jquery-fileupload-rails

Name: rubygem-%{gem_name}
Version: 0.3.4
Release: 1%{?dist}
Summary: jQuery File Upload for Rails 3.1 Asset Pipeline
Group: Development/Languages
License: MIT
URL: https://github.com/tors/jquery-fileupload-rails
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
# BuildRequires: rubygem(rails) >= 3.1
BuildArch: noarch

%description
jQuery File Upload by Sebastian Tschan integrated for Rails 3.1 Asset
Pipeline.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/




# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_instdir}/vendor
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%changelog
* Tue Sep 27 2016 Nick Sabine <nsabine@redhat.com> - 0.3.4-1
- Initial package
