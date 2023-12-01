/* Creacion de tabla */
USE compra_agil;
CREATE TABLE `datos_agil` (
  `id` int(11) NOT NULL,
  `NumeroCotizacion` varchar(255) DEFAULT NULL,
  `Nombre` varchar(255) DEFAULT NULL,
  `Descripcion` text DEFAULT NULL,
  `Direccion` varchar(255) DEFAULT NULL,
  `PlazoEntrega` varchar(50) DEFAULT NULL,
  `Presupuesto` varchar(255) DEFAULT NULL,
  `Fecha` varchar(255) DEFAULT NULL,
  `FechaCierre` varchar(255) DEFAULT NULL,
  `Archivos` varchar(250) DEFAULT NULL
);

/* Procedimiento Almacenado */

BEGIN
    INSERT INTO datos_agil (NumeroCotizacion, Nombre, Descripcion, Direccion, PlazoEntrega, Presupuesto, Fecha, FechaCierre, Archivos)
    SELECT p_NumeroCotizacion, p_Nombre, p_Descripcion, p_Direccion, p_PlazoEntrega, p_Presupuesto, p_Fecha, p_FechaCierre, p_Archivos
    FROM DUAL
    WHERE NOT EXISTS (
        SELECT id FROM datos_agil 
        WHERE NumeroCotizacion = p_NumeroCotizacion 
          AND Nombre = p_Nombre 
          AND Descripcion = p_Descripcion 
          AND Direccion = p_Direccion 
          AND PlazoEntrega = p_PlazoEntrega 
          AND Presupuesto = p_Presupuesto 
          AND Fecha = p_Fecha 
          AND FechaCierre = p_FechaCierre
          AND Archivos = p_Archivos
    );
END