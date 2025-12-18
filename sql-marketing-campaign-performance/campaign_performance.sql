SELECT
  ucm.campana_descripcion AS nombre_campana,
  SUM(uvb.valor_booking)  AS ingresos,
  COUNT(*)                AS viajes_completados
FROM uber_viajes_bookings AS uvb
LEFT JOIN uber_campanas_mercadeo AS ucm
  ON uvb.campana_id = ucm.campana_ID
WHERE uvb.estado_booking = 'Completed'
GROUP BY ucm.campana_descripcion
ORDER BY ingresos DESC;

