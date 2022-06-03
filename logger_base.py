import logging
log = logging  #Import logging as log does the same thing

log.basicConfig(level=log.DEBUG, #Set here the level of debug printing by changing it to debug, info, warning, error and critical
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capa_datos.log'),
                    log.StreamHandler() #consola
                ])

if __name__ == '__main__':
    log.debug('Msg de debug')
    log.info('Imprime info')
    log.warning('Imprime warning')
    log.error('Mensaje de error')
    log.critical('Mensaje de critical')