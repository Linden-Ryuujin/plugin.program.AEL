import unittest, mock, os, sys
from mock import *
from fakes import *

from resources.objects import *

from resources.utils import *
from resources.disk_IO import *

from resources.constants import *

class Test_Launcher(unittest.TestCase):
    
    ROOT_DIR = ''
    TEST_DIR = ''
    TEST_ASSETS_DIR = ''

    @classmethod
    def setUpClass(cls):
        set_log_level(LOG_DEBUG)
        
        cls.TEST_DIR = os.path.dirname(os.path.abspath(__file__))
        cls.ROOT_DIR = os.path.abspath(os.path.join(cls.TEST_DIR, os.pardir))
        cls.TEST_ASSETS_DIR = os.path.abspath(os.path.join(cls.TEST_DIR,'assets/'))
                
        print 'ROOT DIR: {}'.format(cls.ROOT_DIR)
        print 'TEST DIR: {}'.format(cls.TEST_DIR)
        print 'TEST ASSETS DIR: {}'.format(cls.TEST_ASSETS_DIR)
        print '---------------------------------------------------------------------------'

    def _get_test_settings(self):
        
        settings = {}
        settings['lirc_state'] = True
        settings['escape_romfile'] = True
        settings['display_launcher_notify'] = False
        settings['media_state_action'] = 0
        settings['suspend_audio_engine'] = False
        settings['delay_tempo'] = 1
        return settings

    def test_when_creating_a_launcher_with_not_exisiting_id_it_will_fail(self):
        # arrange
        launcher_data = {'id': 'aap'}
        plugin_dir = FakeFile(self.TEST_ASSETS_DIR)

        # act
        factory = LauncherFactory(None, None, plugin_dir)
        actual = factory.create(launcher_data)
        
        # assert
        self.assertIsNone(actual)
                
    @patch('resources.objects.ExecutorFactory')    
    def test_when_its_an_app_factory_loads_with_correct_launcher(self, mock_exeFactory):

        # arrange
        mock_exeFactory.create.return_value = FakeExecutor(None)
        
        launcher_data = {}
        launcher_data['id'] = 'ABC'
        launcher_data['type'] = LAUNCHER_STANDALONE
        launcher_data['application'] = 'path'
        launcher_data['toggle_window'] = True
        launcher_data['romext'] = ''
        launcher_data['application'] = ''
        launcher_data['args'] = ''
        launcher_data['args_extra'] = ''

        settings = {}
        settings['lirc_state'] = True

        # act
        factory = LauncherFactory(settings, mock_exeFactory, FakeFile(self.TEST_ASSETS_DIR))
        launcher = factory.create(launcher_data)
        
        # assert        
        actual = launcher.__class__.__name__
        expected = 'ApplicationLauncher'
        self.assertEqual(actual, expected)
        
    @patch('resources.objects.ExecutorFactory')
    def test_if_app_launcher_will_correctly_passthrough_parameters_when_launching(self, mock_exeFactory):

        # arrange
        expectedApp = 'AbcDefGhiJlkMnoPqrStuVw'
        expectedArgs = 'doop dap dib'

        launcher_data = {}
        launcher_data['id'] = 'ABC'
        launcher_data['type'] = LAUNCHER_STANDALONE
        launcher_data['application'] = expectedApp
        launcher_data['toggle_window'] = True
        launcher_data['args'] = expectedArgs
        launcher_data['m_name'] = 'MyApp'

        settings = self._get_test_settings()
        
        mock = FakeExecutor(None)
        mock_exeFactory.create.return_value = mock

        factory = LauncherFactory(settings, mock_exeFactory, FakeFile(self.TEST_ASSETS_DIR))
        launcher = factory.create(launcher_data)

        # act
        launcher.launch()

        # assert
        self.assertEqual(expectedApp, mock.actualApplication.getOriginalPath())
        self.assertEqual(expectedArgs, mock.actualArgs)
        
    @patch('resources.objects.ExecutorFactory')
    def test_if_app_launcher_will_correctly_alter_arguments_when_launching(self, mock_exeFactory):

        # arrange
        expectedApp = 'C:\Sparta\Action.exe'
        expectedArgs = 'this is C:\Sparta'

        launcher_data = {}
        launcher_data['id'] = 'ABC'
        launcher_data['type'] = 'STANDALONE'
        launcher_data['application'] = expectedApp
        launcher_data['toggle_window'] = True
        launcher_data['args'] = 'this is $apppath%'
        launcher_data['m_name'] = 'MyApp'
        
        mock = FakeExecutor(None)
        mock_exeFactory.create.return_value = mock
        
        settings = self._get_test_settings()

        factory = LauncherFactory(settings, mock_exeFactory, FakeFile(self.TEST_ASSETS_DIR))
        launcher = factory.create(launcher_data)

        # act
        launcher.launch()

        # assert
        self.assertEqual(expectedApp, mock.actualApplication.getOriginalPath())
        self.assertEqual(expectedArgs, mock.actualArgs)
            
    @patch('resources.objects.ExecutorFactory')
    def test_when_using_rom_the_factory_will_get_the_correct_launcher(self, mock_exeFactory):
        
        # arrange
        settings = self._get_test_settings()

        launcher_data = {}
        launcher_data['id'] = 'ABC'
        launcher_data['application'] = 'path'
        launcher_data['type'] = LAUNCHER_ROM
        launcher_data['toggle_window'] = True
        launcher_data['romext'] = ''
        launcher_data['application'] = ''
        launcher_data['args'] = ''
        launcher_data['args_extra'] = ''
        launcher_data['roms_base_noext'] = 'snes'
        
        rom_id = 'fghj'
        rom = { 'id': rom_id, 'm_name': 'TestCase' }
        roms = { rom_id: rom }
        json_data = json.dumps(roms, ensure_ascii = False, indent = 1, separators = (',', ':'))
                
        rom_dir = FakeFile(self.TEST_ASSETS_DIR)
        rom_dir.setFakeContent(json_data)

        # act
        factory = LauncherFactory(settings, mock_exeFactory, rom_dir)
        launcher = factory.create(launcher_data)
        launcher.select_rom(rom_id)
        
        # assert
        actual = launcher.__class__.__name__
        expected = 'StandardRomLauncher'
        self.assertEqual(actual, expected)
                
    @patch('resources.objects.ExecutorFactory')
    def test_if_rom_launcher_will_correctly_passthrough_the_application_when_launching(self, mock_exeFactory):
        
        # arrange
        settings = self._get_test_settings()

        launcher_data= {}
        launcher_data['id'] = 'ABC'
        launcher_data['type'] = LAUNCHER_ROM
        launcher_data['application'] = 'path'
        launcher_data['toggle_window'] = True
        launcher_data['romext'] = ''
        launcher_data['application'] = ''
        launcher_data['args'] = '-a -b -c -d -e $rom$ -yes'
        launcher_data['args_extra'] = ''
        launcher_data['roms_base_noext'] = 'snes'
        
        rom_id = 'fghj'
        rom = { 'id': rom_id, 'm_name': 'TestCase', 'filename':'testing.zip', 'altapp': '', 'altarg': '' }
        roms = { rom_id: rom }
        json_data = json.dumps(roms, ensure_ascii = False, indent = 1, separators = (',', ':'))
                
        rom_dir = FakeFile(self.TEST_ASSETS_DIR)
        rom_dir.setFakeContent(json_data)

        mock = FakeExecutor(None)
        mock_exeFactory.create.return_value = mock

        expected = launcher_data['application']
        expectedArgs = '-a -b -c -d -e testing.zip -yes'

        factory = LauncherFactory(settings, mock_exeFactory, rom_dir)
        launcher = factory.create(launcher_data)
        launcher.select_rom(rom_id)

        # act
        launcher.launch()

        # assert
        self.assertEqual(expected, mock.actualApplication.getOriginalPath())
        self.assertEqual(expectedArgs, mock.actualArgs)
                
    @patch('resources.objects.ExecutorFactory')
    def test_if_rom_launcher_will_use_the_multidisk_launcher_when_romdata_has_disks_field_filled_in(self, mock_exeFactory):
        
        # arrange
        settings = self._get_test_settings()

        launcher_data = {}
        launcher_data['id'] = 'ABC'
        launcher_data['type'] = LAUNCHER_ROM
        launcher_data['application'] = 'path'
        launcher_data['toggle_window'] = True
        launcher_data['romext'] = ''
        launcher_data['application'] = ''
        launcher_data['args'] = ''
        launcher_data['args_extra'] = ''
        launcher_data['roms_base_noext'] = 'snes'
        
        rom_id = 'fghj'
        rom = { 'id': rom_id, 'm_name': 'TestCase', 'disks':['disc01.zip', 'disc02.zip'] }
        roms = { rom_id: rom }
        json_data = json.dumps(roms, ensure_ascii = False, indent = 1, separators = (',', ':'))
        
        rom_dir = FakeFile(self.TEST_ASSETS_DIR)
        rom_dir.setFakeContent(json_data)

        mock = FakeExecutor(None)
        mock_exeFactory.create.return_value = mock

        # act
        factory = LauncherFactory(settings, mock_exeFactory, rom_dir)
        launcher = factory.create(launcher_data)
        launcher.select_rom(rom_id)
        
        # assert        
        actual = launcher.__class__.__name__
        expected = 'StandardRomLauncher'
        self.assertEqual(actual, expected)
                
    @patch('resources.objects.xbmcgui.Dialog.select')
    @patch('resources.objects.ExecutorFactory')
    def test_if_rom_launcher_will_apply_the_correct_disc_in_a_multidisc_situation(self, mock_exeFactory, mock_dialog):

        # arrange
        settings = self._get_test_settings()

        launcher_data = {}
        launcher_data['id'] = 'ABC'
        launcher_data['type'] = LAUNCHER_ROM
        launcher_data['application'] = 'c:\\temp\\'
        launcher_data['toggle_window'] = True
        launcher_data['romext'] = ''
        launcher_data['application'] = ''
        launcher_data['args'] = '-a -b -c -d -e $rom$ -yes'
        launcher_data['args_extra'] = ''
        launcher_data['roms_base_noext'] = 'snes'

        rom = {}
        rom['id'] = 'qqqq'
        rom['m_name'] = 'TestCase'
        rom['filename'] = 'd:\\games\\discXX.zip'
        rom['altapp'] = ''
        rom['altarg'] = ''
        rom['disks'] = ['disc01.zip', 'disc02.zip']
        
        rom_id = rom['id']
        roms = { rom_id: rom }
        json_data = json.dumps(roms, ensure_ascii = False, indent = 1, separators = (',', ':'))
                
        rom_dir = FakeFile(self.TEST_ASSETS_DIR)
        rom_dir.setFakeContent(json_data)

        mock_dialog.return_value = 1
        mock = FakeExecutor(None)
        mock_exeFactory.create.return_value = mock
        
        expected = launcher_data['application']
        expectedArgs = '-a -b -c -d -e d:\\games\\disc02.zip -yes'

        factory = LauncherFactory(settings, mock_exeFactory, rom_dir)
        launcher = factory.create(launcher_data)
        launcher.select_rom(rom_id)

        # act
        launcher.launch()

        # assert
        self.assertEqual(expectedArgs, mock.actualArgs)
    
    @patch('resources.objects.is_windows')
    @patch('resources.objects.is_android')
    @patch('resources.objects.is_linux')    
    @patch('resources.objects.ExecutorFactory')
    def test_if_retroarch_launcher_will_apply_the_correct_arguments_when_running_on_android(self, mock_exeFactory, is_linux_mock,is_android_mock, is_win_mock):
        
        # arrange
        is_linux_mock.return_value = False
        is_win_mock.return_value = False
        is_android_mock.return_value = True
        
        settings = self._get_test_settings()

        launcher_data = {}
        launcher_data['type'] = LAUNCHER_RETROARCH
        launcher_data['id'] = 'ABC'
        launcher_data['toggle_window'] = True
        launcher_data['romext'] = None
        launcher_data['args_extra'] = None
        launcher_data['roms_base_noext'] = 'snes'
        launcher_data['retro_core'] = '/data/data/com.retroarch/cores/mame_libretro_android.so'
        launcher_data['retro_config'] = '/storage/emulated/0/Android/data/com.retroarch/files/retroarch.cfg'
        launcher_data['application'] = None

        rom_id = 'qqqq'
        rom = {}
        rom['id'] = 'qqqq'
        rom['m_name'] = 'TestCase'
        rom['filename'] = 'superrom.zip'
        rom['altapp'] = None
        roms = { rom_id: rom }
        json_data = json.dumps(roms, ensure_ascii = False, indent = 1, separators = (',', ':'))

        rom_dir = FakeFile(self.TEST_ASSETS_DIR)
        rom_dir.setFakeContent(json_data)

        mock = FakeExecutor(None)
        mock_exeFactory.create.return_value = mock

        expected = '/system/bin/am'
        expectedArgs = "start --user 0 -a android.intent.action.MAIN -c android.intent.category.LAUNCHER -n com.retroarch/.browser.retroactivity.RetroActivityFuture -e ROM 'superrom.zip' -e LIBRETRO /data/data/com.retroarch/cores/mame_libretro_android.so -e CONFIGFILE /storage/emulated/0/Android/data/com.retroarch/files/retroarch.cfg "

        factory = LauncherFactory(settings, mock_exeFactory, rom_dir)
        launcher = factory.create(launcher_data)
        launcher.select_rom(rom_id)

        # act
        launcher.launch()

        # assert
        self.assertEqual(expected, mock.getActualApplication().getPath())
        self.assertEqual(expectedArgs, mock.actualArgs)
        
    @patch('resources.objects.is_windows')
    @patch('resources.objects.is_android')
    @patch('resources.objects.is_linux')    
    @patch('resources.objects.ExecutorFactory')
    def test_loading_the_roms_of_launcher_works_correctly(self, mock_exeFactory, is_linux_mock,is_android_mock, is_win_mock):
        
        # arrange
        is_linux_mock.return_value = False
        is_win_mock.return_value = False
        is_android_mock.return_value = True
        
        settings = self._get_test_settings()

        launcher_data = {}
        launcher_data['type'] = LAUNCHER_RETROARCH
        launcher_data['id'] = 'ABC'
        launcher_data['toggle_window'] = True
        launcher_data['romext'] = None
        launcher_data['args_extra'] = None
        launcher_data['roms_base_noext'] = 'roms_Sega_32X_518519'
        launcher_data['application'] = 'app'

        mock = FakeExecutor(None)
        mock_exeFactory.create.return_value = mock
                
        rom_dir = StandardFileName(self.TEST_ASSETS_DIR)
        repository = RomSetRepository(rom_dir)
        target = StandardRomLauncher(launcher_data, settings, mock_exeFactory, repository, None, False)
        
        expected = 35

        # act
        actual = target.get_roms()

        # assert
        self.assertIsNotNone(actual)
        self.assertEqual(len(actual), expected)
 
    @patch('resources.objects.is_windows')
    @patch('resources.objects.is_android')
    @patch('resources.objects.is_linux')    
    @patch('resources.objects.ExecutorFactory')
    def test_loading_the_roms_filtered_of_launcher_works_correctly(self, mock_exeFactory, is_linux_mock,is_android_mock, is_win_mock):
        
        # arrange
        is_linux_mock.return_value = False
        is_win_mock.return_value = False
        is_android_mock.return_value = True
        
        settings = self._get_test_settings()

        launcher_data = {}
        launcher_data['type'] = LAUNCHER_RETROARCH
        launcher_data['id'] = 'ABC'
        launcher_data['toggle_window'] = True
        launcher_data['romext'] = None
        launcher_data['args_extra'] = None
        launcher_data['roms_base_noext'] = 'roms_Sega_32X_518519'
        launcher_data['application'] = 'app'

        mock = FakeExecutor(None)
        mock_exeFactory.create.return_value = mock

        rom_dir = StandardFileName(self.TEST_ASSETS_DIR)
        repository = RomSetRepository(rom_dir)
        target = StandardRomLauncher(launcher_data, settings, mock_exeFactory, repository, None, False)

        expected = 35

        # act
        actual = target.get_roms_filtered()

        # assert
        self.assertIsNotNone(actual)
        self.assertEqual(len(actual), expected)

if __name__ == '__main__':
   unittest.main()
