# Arc Theme for GNOME 49

Arc is a flat GTK and desktop theme designed by horst3180. This fork builds on jnsh’s 20221218 release. It adds light and dark GNOME Shell 49 themes and an optional Arc Dark stylesheet for GTK 4 / libadwaita apps, including GNOME Settings and GNOME-drawn title bars on X11 apps such as Jasper. [Original Arc](https://github.com/horst3180/arc-theme) · [20221218 release](https://github.com/jnsh/arc-theme/releases/tag/20221218)

## Install on GNOME 49

Tested on Gentoo with GNOME Shell 49.7, GTK 4.20.4 and libadwaita 1.8.7. Install Git, Meson, Ninja, sassc, Python 3.8 or later, and GLib’s `glib-compile-resources`. Run these commands as your desktop user.

```sh
git clone https://github.com/an0nn30/arc-theme.git
cd arc-theme
meson setup build --prefix="$HOME/.local" -Dthemes=gnome-shell,gtk4 -Dvariants=light,dark
meson compile -C build
meson install -C build
```

Enable the [User Themes extension](https://extensions.gnome.org/extension/19/user-themes/), then choose **Arc** or **Arc-Dark** under **Shell** in GNOME Tweaks. The build detects the installed Shell version. For a packaging build, pass `-Dgnome_shell_version=49`.

### Arc Dark in native apps

From the checkout, run the following to select Arc Dark for theme-aware apps and install the dark palette and window controls for libadwaita.

```sh
gsettings set org.gnome.desktop.interface gtk-theme 'Arc-Dark'
gsettings set org.gnome.desktop.interface color-scheme 'prefer-dark'
python3 common/gtk-4.0/libadwaita/install-app-theme.py
```

Reopen Settings and other GTK 4 apps. Sign out of GNOME and back in to reload the window frames that Mutter draws for XWayland apps. Jasper’s **Desktop Colors** setting styles its menus and tabs.

The installer prepends one import to `$XDG_CONFIG_HOME/gtk-4.0/gtk.css` (normally `~/.config/gtk-4.0/gtk.css`). It applies in dark mode with normal contrast, even if you later select a different dark theme. To undo the override, remove the line `@import url("arc-dark-49-apps.css");` and reopen the apps.

For GTK 3 apps such as Nemo, install your distribution’s Arc GTK 3 theme, or add `gtk3` to the Meson theme list and install Inkscape to render the GTK 3 assets.

## Arc is available in four variants

##### Arc

![A screenshot of the Arc theme](.github/arc-prv.png)

##### Arc-Darker

![A screenshot of the Arc-Darker theme](.github/arc-darker-prv.png)

##### Arc-Dark

![A screenshot of the Arc-Dark theme](.github/arc-dark-prv.png)

##### Arc-Lighter

![A screenshot of the Arc-Lighter theme](.github/arc-lighter-prv.png)

## Supported toolkits and desktops

Arc comes with themes for the following:
* GTK 2
* GTK 3
* GTK 4
* GNOME Shell 3.28–3.38, 40–43 and 49
* Cinnamon >=3.8
* Unity
* Metacity
* Xfwm
* Plank

## Installation

#### Packages

Arc Theme is available from the official software package repositories for many common Linux distributions and FOSS operating systems. Installing the theme by using the package manager of your operating system should be the preferred method in most cases.

See [the wiki](https://github.com/jnsh/arc-theme/wiki/Packages) for non-exhaustive list of distribution packages, and some additional packages.

#### Manual installation

For installing the theme by compiling it from the source code, see [INSTALL.md](INSTALL.md) for build instructions, list of dependencies, build options and additional details.

## Issues

If you are experiencing any kind of issues, found a bug, or have a suggestion for improving the theme, please open an issue at <https://github.com/an0nn30/arc-theme/issues>.

Some known issues are addressed in [common problems](https://github.com/jnsh/arc-theme/wiki/Common-problems).

## Contributing

If you'd like to contribute to the project, open an pull request, or an issue for discussion. See [HACKING.md](HACKING.md) for further details.

## License

Arc is available under the terms of the GPL-3.0. See [COPYING](COPYING) for details. The GNOME 49 component includes GNOME Shell Sass and its [upstream notices](common/gnome-shell/49/README.md).

## Full Preview

![A full screenshot of the Arc theme](http://i.imgur.com/tD1OBQ3.png)
<sub>Screenshot Details: Icons: [Arc](https://github.com/horst3180/arc-icon-theme) | Launcher Icons based on [White Pixel Icons](http://darkdawg.deviantart.com/art/White-Pixel-Icons-252310560) | [Wallpaper](https://pixabay.com/photo-869593/) | Font: Futura Bk bt</sub>
