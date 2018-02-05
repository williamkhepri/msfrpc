#!/usr/bin/env python
# MSF-RPC - Una librería python para facilitar la comunicación MSG-RPC con Metasploit
# Ryan Linn  - RLinn@trustwave.com
# Copyright (C) 2011 Trustwave
# Este programa es software libre: puede redistribuirlo y / o modificarlo bajo los términos de la Licencia Pública General de GNU publicada por la Free Software Foundation, ya sea la versión 3 de la Licencia, o (a su elección) cualquier versión posterior.

# Este programa se distribuye con la esperanza de que sea útil, pero SIN NINGUNA GARANTÍA; sin siquiera la garantía implícita de COMERCIABILIDAD o IDONEIDAD PARA UN PROPÓSITO PARTICULAR. Ver la Licencia Pública General de GNU para más detalles.

# Debería haber recibido una copia de la Licencia Pública General de GNU junto con este programa. De lo contrario, consulte <http://www.gnu.org/licenses/>.

import msfrpc

if __name__ == '__main__':
  
  # Cree una nueva instancia del cliente Msfrpc con las opciones predeterminadas
  client = msfrpc.Msfrpc({})

  # Inicie sesión en el servidor msfmsg con la contraseña "abc123"
  client.login('msf','abc123')

  # Obtenga una lista de los exploits del servidor
  mod = client.call('module.exploits')
  
  # Toma el primer elemento del valor de los módulos del diccionario devuelto
  print "Compatible payloads for : %s\n" % mod['modules'][0]
  
  # Obtenga la lista de cargas útiles compatibles para la primera opción
  ret = client.call('module.compatible_payloads',[mod['modules'][0]])
  for i in (ret.get('payloads')):
    print "\t%s" % i

