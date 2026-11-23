{
  lib,
  python3Packages,
}:
python3Packages.buildPythonApplication (finalAttrs: {
  pname = "asu";
  version = "0.1.0";

  src = with lib.fileset; toSource {
    root = ../../asu;
    fileset = unions [
      ../../asu/src
      ../../asu/pyproject.toml
    ];
  };

  pyproject = true;

  build-system = with python3Packages; [
    hatchling
  ];

  meta = with lib; {
    description = "Generate an AltStore source file for my apps";
    homepage = "https://github.com/Frontear/altstore-sources";

    license = licenses.agpl3Plus;
    maintainers = with maintainers; [ frontear ];
    platforms = platforms.linux;

    mainProgram = "asu";
  };
})