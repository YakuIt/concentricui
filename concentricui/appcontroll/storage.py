from os import mkdir, path

from kivy.app import App
from kivy.storage.dictstore import DictStore


class BackupDictStore(DictStore):

    def __init__(self, filename, original=None, **kwargs):
        self.filename = filename
        self._data = original._data

        self._is_changed = True
        self.store_sync()

        super(DictStore, self).__init__(**kwargs)


def get_store(store_name, subfolder=None, as_backup=False, from_backup=False):
    app = App.get_running_app()

    #  remove .pydict
    if store_name.endswith('.pydict'):
        store_name.strip('.pydict')

    #  add _backup if its a backup
    if from_backup:
        store_name += '_backup'

    #  always add .pydict (as it was removed if it existed)
    store_name += '.pydict'

    if not subfolder:
        #  get the path (straightforward)
        store_path = path.join(app.user_data_dir, store_name)
    else:
        #  get the subfolder's path
        folder_path = path.join(app.user_data_dir, subfolder)
        try:
            #  try to make the subfolder
            mkdir(folder_path)
        except:
            #  if it already exists then simply print the line bellow and do nothing else
            print('i guess its already made')

        #  get the store's path
        store_path = path.join(folder_path, store_name)

    #  return the correct storage type
    if as_backup is True:
        #  if as_backup is simply True, then try to get the store with the same name
        #  this is a little inefficient but who cares really
        store = get_store(store_name, subfolder)
        return BackupDictStore(store_path, store)
    elif as_backup:
        #  if as_backup is specified then backup from the specified store
        return BackupDictStore(store_path, as_backup)
    else:  # if not as backup...., just open a normal store
        return DictStore(store_path)


def get_store_with_backup(store_name, subfolder=None):
    # this wont get it again if it changed... but why would it ever change
    try:
        #  this is if it works:
        #  get the store, and back it up as the backup store
        store = get_store(store_name, subfolder)
        backup_store = get_store(store_name, subfolder, from_backup=True, as_backup=store)

    except:
        #  fixme except the specific error
        #  if it doesnt work it is most likely because the store was corrupt
        #  in this case set the store to be the backup store
        backup_store = get_store(store_name, subfolder, from_backup=True, as_backup=False)
        store = get_store(store_name, subfolder, from_backup=False, as_backup=backup_store)

    return store, backup_store
