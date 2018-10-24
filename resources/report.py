# -*- coding: utf-8 -*-
#
# Advanced Emulator Launcher platform and emulator information
#

# Copyright (c) 2016-2018 Wintermute0110 <wintermute0110@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# --- Python standard library ---
from __future__ import unicode_literals
from __future__ import division
import abc

# --- AEL modules ---
from utils import *

#
# This must be implemented as a list of strings. See AML for more details.
#
def report_print_ROM(slist, rom):
    slist.append('')
    slist.append("[COLOR violet]id[/COLOR]: '{0}'".format(rom.get_id()))
    # >> Metadata
    slist.append("[COLOR violet]m_name[/COLOR]: '{0}'".format(rom.get_name()))
    slist.append("[COLOR violet]m_year[/COLOR]: '{0}'".format(rom.get_releaseyear()))
    slist.append("[COLOR violet]m_genre[/COLOR]: '{0}'".format(rom.get_genre()))
    slist.append("[COLOR violet]m_developer[/COLOR]: '{0}'".format(rom.get_developer()))
    slist.append("[COLOR violet]m_nplayers[/COLOR]: '{0}'".format(rom.get_number_of_players()))
    slist.append("[COLOR violet]m_esrb[/COLOR]: '{0}'".format(rom.get_esrb_rating()))
    slist.append("[COLOR violet]m_rating[/COLOR]: '{0}'".format(rom.get_rating()))
    slist.append("[COLOR violet]m_plot[/COLOR]: '{0}'".format(rom.get_plot()))
    # >> Info
    slist.append("[COLOR violet]filename[/COLOR]: '{0}'".format(rom.get_filename()))
    slist.append("[COLOR skyblue]disks[/COLOR]: {0}".format(rom.get_disks()))
    slist.append("[COLOR violet]altapp[/COLOR]: '{0}'".format(rom.get_alternative_application()))
    slist.append("[COLOR violet]altarg[/COLOR]: '{0}'".format(rom.get_alternative_arguments()))
    slist.append("[COLOR skyblue]finished[/COLOR]: {0}".format(rom.is_finished()))
    slist.append("[COLOR violet]nointro_status[/COLOR]: '{0}'".format(rom.get_nointro_status()))
    slist.append("[COLOR violet]pclone_status[/COLOR]: '{0}'".format(rom.get_pclone_status()))
    slist.append("[COLOR violet]cloneof[/COLOR]: '{0}'".format(rom.get_clone()))
    # >> Assets/artwork
    asset_infos = self.assetFactory.get_asset_kinds_for_roms()
    for asset_info in asset_infos:
        slist.append("[COLOR violet]{0}[/COLOR]: '{1}'".format(asset_info.key, rom.get_asset(asset_info)))

    return info_text

def report_print_ROM_additional(slist, rom):
    slist.append('')
    slist.append("[COLOR violet]launcherID[/COLOR]: '{0}'".format(rom['launcherID']))
    slist.append("[COLOR violet]platform[/COLOR]: '{0}'".format(rom['platform']))
    slist.append("[COLOR violet]application[/COLOR]: '{0}'".format(rom['application']))
    slist.append("[COLOR violet]args[/COLOR]: '{0}'".format(rom['args']))
    slist.append("[COLOR skyblue]args_extra[/COLOR]: {0}".format(rom['args_extra']))
    slist.append("[COLOR violet]rompath[/COLOR]: '{0}'".format(rom['rompath']))
    slist.append("[COLOR violet]romext[/COLOR]: '{0}'".format(rom['romext']))
    slist.append("[COLOR skyblue]toggle_window[/COLOR]: {0}".format(rom['toggle_window']))
    slist.append("[COLOR skyblue]non_blocking[/COLOR]: {0}".format(rom['non_blocking']))
    slist.append("[COLOR violet]roms_default_icon[/COLOR]: '{0}'".format(rom['roms_default_icon']))
    slist.append("[COLOR violet]roms_default_fanart[/COLOR]: '{0}'".format(rom['roms_default_fanart']))
    slist.append("[COLOR violet]roms_default_banner[/COLOR]: '{0}'".format(rom['roms_default_banner']))
    slist.append("[COLOR violet]roms_default_poster[/COLOR]: '{0}'".format(rom['roms_default_poster']))
    slist.append("[COLOR violet]roms_default_clearlogo[/COLOR]: '{0}'".format(rom['roms_default_clearlogo']))

    # >> Favourite ROMs unique fields.
    slist.append("[COLOR violet]fav_status[/COLOR]: '{0}'".format(rom['fav_status']))
    # >> 'launch_count' only in Favourite ROMs in "Most played ROMs"
    if 'launch_count' in rom:
        slist.append("[COLOR skyblue]launch_count[/COLOR]: {0}".format(rom['launch_count']))

def report_print_Launcher(slist, launcher):
    launcher_data = launcher.get_data()

    slist.append('')
    slist.append("[COLOR violet]id[/COLOR]: '{0}'".format(launcher_data['id']))
    slist.append("[COLOR violet]m_name[/COLOR]: '{0}'".format(launcher_data['m_name']))
    slist.append("[COLOR violet]m_year[/COLOR]: '{0}'".format(launcher_data['m_year']))
    slist.append("[COLOR violet]m_genre[/COLOR]: '{0}'".format(launcher_data['m_genre']))
    slist.append("[COLOR violet]m_developer[/COLOR]: '{0}'".format(launcher_data['m_developer']))
    slist.append("[COLOR violet]m_rating[/COLOR]: '{0}'".format(launcher_data['m_rating']))
    slist.append("[COLOR violet]m_plot[/COLOR]: '{0}'".format(launcher_data['m_plot']))

    slist.append("[COLOR violet]platform[/COLOR]: '{0}'".format(launcher_data['platform']))
    slist.append("[COLOR violet]categoryID[/COLOR]: '{0}'".format(launcher_data['categoryID']))
    slist.append("[COLOR violet]application[/COLOR]: '{0}'".format(launcher_data['application']))
    slist.append("[COLOR violet]args[/COLOR]: '{0}'".format(launcher_data['args']))
    slist.append("[COLOR skyblue]args_extra[/COLOR]: {0}".format(launcher_data['args_extra']))
    slist.append("[COLOR violet]rompath[/COLOR]: '{0}'".format(launcher_data['rompath']))
    slist.append("[COLOR violet]romext[/COLOR]: '{0}'".format(launcher_data['romext']))
    # Bool settings
    slist.append("[COLOR skyblue]finished[/COLOR]: {0}".format(launcher_data['finished']))
    slist.append("[COLOR skyblue]toggle_window[/COLOR]: {0}".format(launcher_data['toggle_window']))
    slist.append("[COLOR skyblue]non_blocking[/COLOR]: {0}".format(launcher_data['non_blocking']))
    slist.append("[COLOR skyblue]multidisc[/COLOR]: {0}".format(launcher_data['multidisc']))

    slist.append("[COLOR violet]roms_base_noext[/COLOR]: '{0}'".format(launcher_data['roms_base_noext']))
    slist.append("[COLOR violet]nointro_xml_file[/COLOR]: '{0}'".format(launcher_data['nointro_xml_file']))
    slist.append("[COLOR violet]nointro_display_mode[/COLOR]: '{0}'".format(launcher_data['nointro_display_mode']))
    slist.append("[COLOR violet]launcher_display_mode[/COLOR]: '{0}'".format(launcher_data['launcher_display_mode']))
    slist.append("[COLOR skyblue]num_roms[/COLOR]: {0}".format(launcher_data['num_roms']))
    slist.append("[COLOR skyblue]num_parents[/COLOR]: {0}".format(launcher_data['num_parents']))
    slist.append("[COLOR skyblue]num_clones[/COLOR]: {0}".format(launcher_data['num_clones']))
    slist.append("[COLOR skyblue]num_have[/COLOR]: {0}".format(launcher_data['num_have']))
    slist.append("[COLOR skyblue]num_miss[/COLOR]: {0}".format(launcher_data['num_miss']))
    slist.append("[COLOR skyblue]num_unknown[/COLOR]: {0}".format(launcher_data['num_unknown']))
    slist.append("[COLOR skyblue]timestamp_launcher_data[/COLOR]: {0}".format(launcher_data['timestamp_launcher']))
    slist.append("[COLOR skyblue]timestamp_report[/COLOR]: {0}".format(launcher_data['timestamp_report']))

    slist.append("[COLOR violet]default_icon[/COLOR]: '{0}'".format(launcher_data['default_icon']))
    slist.append("[COLOR violet]default_fanart[/COLOR]: '{0}'".format(launcher_data['default_fanart']))
    slist.append("[COLOR violet]default_banner[/COLOR]: '{0}'".format(launcher_data['default_banner']))
    slist.append("[COLOR violet]default_poster[/COLOR]: '{0}'".format(launcher_data['default_poster']))
    slist.append("[COLOR violet]default_clearlogo[/COLOR]: '{0}'".format(launcher_data['default_clearlogo']))
    slist.append("[COLOR violet]default_controller[/COLOR]: '{0}'".format(launcher_data['default_controller']))
    slist.append("[COLOR violet]Asset_Prefix[/COLOR]: '{0}'".format(launcher_data['Asset_Prefix']))
    slist.append("[COLOR violet]s_icon[/COLOR]: '{0}'".format(launcher_data['s_icon']))
    slist.append("[COLOR violet]s_fanart[/COLOR]: '{0}'".format(launcher_data['s_fanart']))
    slist.append("[COLOR violet]s_banner[/COLOR]: '{0}'".format(launcher_data['s_banner']))
    slist.append("[COLOR violet]s_poster[/COLOR]: '{0}'".format(launcher_data['s_poster']))
    slist.append("[COLOR violet]s_clearlogo[/COLOR]: '{0}'".format(launcher_data['s_clearlogo']))
    slist.append("[COLOR violet]s_controller[/COLOR]: '{0}'".format(launcher_data['s_controller']))
    slist.append("[COLOR violet]s_trailer[/COLOR]: '{0}'".format(launcher_data['s_trailer']))

    slist.append("[COLOR violet]roms_default_icon[/COLOR]: '{0}'".format(launcher_data['roms_default_icon']))
    slist.append("[COLOR violet]roms_default_fanart[/COLOR]: '{0}'".format(launcher_data['roms_default_fanart']))
    slist.append("[COLOR violet]roms_default_banner[/COLOR]: '{0}'".format(launcher_data['roms_default_banner']))
    slist.append("[COLOR violet]roms_default_poster[/COLOR]: '{0}'".format(launcher_data['roms_default_poster']))
    slist.append("[COLOR violet]roms_default_clearlogo[/COLOR]: '{0}'".format(launcher_data['roms_default_clearlogo']))
    slist.append("[COLOR violet]ROM_asset_path[/COLOR]: '{0}'".format(launcher_data['ROM_asset_path']))
    slist.append("[COLOR violet]path_title[/COLOR]: '{0}'".format(launcher_data['path_title']))
    slist.append("[COLOR violet]path_snap[/COLOR]: '{0}'".format(launcher_data['path_snap']))
    slist.append("[COLOR violet]path_boxfront[/COLOR]: '{0}'".format(launcher_data['path_boxfront']))
    slist.append("[COLOR violet]path_boxback[/COLOR]: '{0}'".format(launcher_data['path_boxback']))
    slist.append("[COLOR violet]path_cartridge[/COLOR]: '{0}'".format(launcher_data['path_cartridge']))
    slist.append("[COLOR violet]path_fanart[/COLOR]: '{0}'".format(launcher_data['path_fanart']))
    slist.append("[COLOR violet]path_banner[/COLOR]: '{0}'".format(launcher_data['path_banner']))
    slist.append("[COLOR violet]path_clearlogo[/COLOR]: '{0}'".format(launcher_data['path_clearlogo']))
    slist.append("[COLOR violet]path_flyer[/COLOR]: '{0}'".format(launcher_data['path_flyer']))
    slist.append("[COLOR violet]path_map[/COLOR]: '{0}'".format(launcher_data['path_map']))
    slist.append("[COLOR violet]path_manual[/COLOR]: '{0}'".format(launcher_data['path_manual']))
    slist.append("[COLOR violet]path_trailer[/COLOR]: '{0}'".format(launcher_data['path_trailer']))

def report_print_Category(slist, category):
    slist.append('')
    slist.append("[COLOR violet]id[/COLOR]: '{0}'".format(category['id']))
    slist.append("[COLOR violet]m_name[/COLOR]: '{0}'".format(category['m_name']))
    slist.append("[COLOR violet]m_year[/COLOR]: '{0}'".format(category['m_year']))
    slist.append("[COLOR violet]m_genre[/COLOR]: '{0}'".format(category['m_genre']))
    slist.append("[COLOR violet]m_developer[/COLOR]: '{0}'".format(category['m_developer']))
    slist.append("[COLOR violet]m_rating[/COLOR]: '{0}'".format(category['m_rating']))
    slist.append("[COLOR violet]m_plot[/COLOR]: '{0}'".format(category['m_plot']))
    slist.append("[COLOR skyblue]finished[/COLOR]: {0}".format(category['finished']))
    slist.append("[COLOR violet]default_icon[/COLOR]: '{0}'".format(category['default_icon']))
    slist.append("[COLOR violet]default_fanart[/COLOR]: '{0}'".format(category['default_fanart']))
    slist.append("[COLOR violet]default_banner[/COLOR]: '{0}'".format(category['default_banner']))
    slist.append("[COLOR violet]default_poster[/COLOR]: '{0}'".format(category['default_poster']))
    slist.append("[COLOR violet]default_clearlogo[/COLOR]: '{0}'".format(category['default_clearlogo']))
    slist.append("[COLOR violet]Asset_Prefix[/COLOR]: '{0}'".format(category['Asset_Prefix']))
    slist.append("[COLOR violet]s_icon[/COLOR]: '{0}'".format(category['s_icon']))
    slist.append("[COLOR violet]s_fanart[/COLOR]: '{0}'".format(category['s_fanart']))
    slist.append("[COLOR violet]s_banner[/COLOR]: '{0}'".format(category['s_banner']))
    slist.append("[COLOR violet]s_poster[/COLOR]: '{0}'".format(category['s_poster']))
    slist.append("[COLOR violet]s_clearlogo[/COLOR]: '{0}'".format(category['s_clearlogo']))
    slist.append("[COLOR violet]s_trailer[/COLOR]: '{0}'".format(category['s_trailer']))

def report_print_Collection(slist, collection):
    slist.append('')
    slist.append("[COLOR violet]id[/COLOR]: '{0}'".format(collection['id']))
    slist.append("[COLOR violet]m_name[/COLOR]: '{0}'".format(collection['m_name']))
    slist.append("[COLOR violet]m_genre[/COLOR]: '{0}'".format(collection['m_genre']))
    slist.append("[COLOR violet]m_rating[/COLOR]: '{0}'".format(collection['m_rating']))
    slist.append("[COLOR violet]m_plot[/COLOR]: '{0}'".format(collection['m_plot']))
    slist.append("[COLOR violet]roms_base_noext[/COLOR]: {0}".format(collection['roms_base_noext']))
    slist.append("[COLOR violet]default_icon[/COLOR]: '{0}'".format(collection['default_icon']))
    slist.append("[COLOR violet]default_fanart[/COLOR]: '{0}'".format(collection['default_fanart']))
    slist.append("[COLOR violet]default_banner[/COLOR]: '{0}'".format(collection['default_banner']))
    slist.append("[COLOR violet]default_poster[/COLOR]: '{0}'".format(collection['default_poster']))
    slist.append("[COLOR violet]default_clearlogo[/COLOR]: '{0}'".format(collection['default_clearlogo']))
    slist.append("[COLOR violet]s_icon[/COLOR]: '{0}'".format(collection['s_icon']))
    slist.append("[COLOR violet]s_fanart[/COLOR]: '{0}'".format(collection['s_fanart']))
    slist.append("[COLOR violet]s_banner[/COLOR]: '{0}'".format(collection['s_banner']))
    slist.append("[COLOR violet]s_poster[/COLOR]: '{0}'".format(collection['s_poster']))
    slist.append("[COLOR violet]s_clearlogo[/COLOR]: '{0}'".format(collection['s_clearlogo']))
    slist.append("[COLOR violet]s_trailer[/COLOR]: '{0}'".format(collection['s_trailer']))

class Reporter(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, launcher_data, decoratorReporter = None):

        self.launcher_data = launcher_data
        self.decoratorReporter = decoratorReporter

    @abc.abstractmethod
    def open(self):
        pass
    
    @abc.abstractmethod
    def close(self):
        pass

    @abc.abstractmethod
    def _write_message(self, message):
        pass

    def write(self, message):
        
        self._write_message(message)

        if self.decoratorReporter:
            self.decoratorReporter.write(message)

class LogReporter(Reporter):
    def open(self, report_title):
        return super(LogReporter, self).close()

    def close(self):
        return super(LogReporter, self).close()

    def _write_message(self, message):
        log_info(message)

class FileReporter(Reporter):
    def __init__(self, reports_dir, launcher_data, decoratorReporter = None):
        self.report_file = reports_dir.pjoin(launcher_data['roms_base_noext'] + '_report.txt')
        super(FileReporter, self).__init__(launcher_data, decoratorReporter)

    def open(self, report_title):
        log_info('Report file OP "{0}"'.format(self.report_file.getOriginalPath()))
        self.report_file.open('w')

        # --- Get information from launcher ---
        launcher_path = FileNameFactory.create(self.launcher_data['rompath'])
        
        self.write('******************** Report: {} ...  ********************'.format(report_title))
        self.write('  Launcher name "{0}"'.format(self.launcher_data['m_name']))
        self.write('  Launcher type "{0}"'.format(self.launcher_data['type'] if 'type' in self.launcher_data else 'Unknown'))
        self.write('  launcher ID   "{0}"'.format(self.launcher_data['id']))
        self.write('  ROM path      "{0}"'.format(launcher_path.getPath()))
        self.write('  ROM ext       "{0}"'.format(self.launcher_data['romext']))
        self.write('  Platform      "{0}"'.format(self.launcher_data['platform']))
        self.write(  'Multidisc     "{0}"'.format(self.launcher_data['multidisc']))

    def close(self):
        self.report_file.close()

    def _write_message(self, message):
        self.report_file.write(message.encode('utf-8'))
        self.report_file.write('\n'.encode('utf-8'))
