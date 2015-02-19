from pbf.Commands.command_manager import CommandConfig, RegisterCommands

commands = [CommandConfig("insert setup-package", "pbf_python.Commands.insert_setup_package.InsertSetupPackage", description="Inserts a package into the setup package"),
            CommandConfig("mk pydir", "pbf_python.Commands.mk_pydir.MakePyDir", description="Makes a Python Directory"),
            CommandConfig("new class", "pbf_python.Commands.new_class.NewClass", description="Create a new Python Class"),
            CommandConfig("new main", "pbf_python.Commands.new_main.NewMain", description="Create a new Python main file")]

RegisterCommands(commands)