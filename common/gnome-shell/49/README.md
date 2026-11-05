# GNOME Shell 49 sources

The Sass, Shell resource images, pad OSD styles and stock high-contrast stylesheet come from the [GNOME Shell 49.7 source release](https://download.gnome.org/sources/gnome-shell/49/gnome-shell-49.7.tar.xz) (SHA-256 `4967c50a9b01618c2522d440bc4e90551648ec1a59114a6b61157a655403d88f`). The upstream Sass includes [GPL-2.0-or-later notices](sass/gnome-shell-sass/README.md). The common stylesheet also carries an [LGPL-2.1 notice](sass/gnome-shell-sass/COPYING.LGPL-2.1).

This port imports Arc’s existing Shell 43 palette and adapts the accent colors, panel, controls, menus and notifications to the GNOME 49 widget tree. Optional compiled Shell resources include GNOME’s stock high-contrast stylesheet. The GTK 4 artwork comes from the [Arc 20221218 release](https://github.com/jnsh/arc-theme/releases/tag/20221218) alongside its editable SVG in `common/gtk-4.0/assets`.
