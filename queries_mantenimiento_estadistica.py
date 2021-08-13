# queries directas de los indicadores a la bbdd



#-------------------------
# Nº total_dist_vehiculos_MC
total_dist_v_mc = """select count(distinct(txt_matricula)) 
                            from t_transito 
                            where tms_transito::date = '%s'"""

# Nº total_dist_vehiculos_acceso_Park
total_dist_v_acceso_park = """select count(distinct(txt_matricula))
                                    , u.nom_usuario 
                               from t_usuario u join t_acceso_parking ap using (cod_usuario) 
                               where u.cod_usuario in  (559, 558, 694, 693, 747, 746, 639, 640, 459, 458, 676, 675, 455, 454, 520, 519, 368, 367, 429, 428) 
                                    and ap.tmp_acceso::date = '%s' 
                            group by 2"""

# Nº total_dist_vehiculos_hab_acceso_MC
total_dist_v_hab_acceso_mc = """WITH habituales AS 
	                                    (SELECT count(*)
		                                    , txt_matricula
		                                    , cod_usuario
		                                    from public.ft_acceso_parking_internet
		                                    WHERE cod_usuario in (559, 558, 694, 693, 747, 746, 639, 640, 459, 458, 676, 675, 455, 454, 520, 519, 368, 367, 429, 428)
		                                        AND tmp_acceso >= '%s' 
		                                GROUP BY 2 , 3
		                                HAVING COUNT(*) > %s) 
	                            SELECT count(distinct(t.txt_matricula)), habituales.cod_usuario
		                            FROM public.t_transito t
			                        JOIN public.mv_vehiculo_distintivo_ambiental mvda USING ( txt_matricula )
			                        JOIN habituales USING ( txt_matricula ) JOIN public.t_sancion s USING ( cod_transito )
		                            WHERE  t.cod_pdc <> 116
			                            AND mvda.cod_distintivo_ambiental <> 9
			                            AND s.fec_sancion = '%s'
		                        group by 2"""

# Nº total_dist_vehiculos_sancionables_hab_acceso_MC
total_dist_v_sancionables_hab_acceso_mc = """WITH habituales AS
	                                                (SELECT count(*)
		                                                    , txt_matricula
		                                                    , cod_usuario
		                                                FROM public.ft_acceso_parking_internet
		                                                WHERE cod_usuario in (559, 558, 694, 693, 747, 746, 639, 640, 459, 458, 676, 675, 455, 454, 520, 519, 368, 367, 429, 428)
		                                                    AND tmp_acceso >= '%s' 
		                                            GROUP BY 2, 3
		                                            HAVING COUNT(*) > %s)
	                                        SELECT count(distinct(txt_matricula))
	                                                , habituales.cod_usuario
		                                        FROM public.t_transito t
			                                    JOIN public.mv_vehiculo_distintivo_ambiental mvda USING ( txt_matricula )
			                                    JOIN habituales USING ( txt_matricula ) 
			                                    JOIN public.t_sancion s USING ( cod_transito )
		                                        WHERE  s.cod_estado_sancion in (1, 5)
			                                        AND t.cod_pdc <> 116
			                                        AND mvda.cod_distintivo_ambiental <> 9
			                                        AND s.fec_sancion = '%s'
			                                group by 2"""


# Nº total_dist_vehiculos_hab_acceso_Park
total_dist_v_hab_acceso_park = """WITH habituales AS
	                                        (SELECT count(*)
		                                            , txt_matricula
		                                            , cod_usuario
		                                        FROM t_acceso_parking
		                                        WHERE cod_usuario in (559, 558, 694, 693, 747, 746, 639, 640, 459, 458, 676, 675, 455, 454, 520, 519, 368, 367, 429, 428)
		                                        AND tmp_acceso >= '%s' 
		                                    GROUP BY 2, 3
		                                    HAVING COUNT(*) > %s) 
	                                SELECT count(distinct(txt_matricula)), cod_usuario
		                                FROM t_acceso_parking
		                                WHERE tmp_acceso::date = '%s'
		                                    and cod_estado_movimiento not in (5, 6)
		                                    and cod_usuario in (559, 558, 694, 693, 747, 746, 639, 640, 459, 458, 676, 675, 455, 454, 520, 519, 368, 367, 429, 428)
		                            group by 2"""

# Nº_vehiculos_con_transito_sancionable_SIN_acceso_Park
total_v_sancionables_sin_acceso_park = """WITH habituales AS 
	(SELECT count(*)
		, txt_matricula 
		FROM public.ft_acceso_parking_internet 
		WHERE cod_usuario in (559, 558, 694, 693, 747, 746, 639, 640, 459, 458, 676, 675, 455, 454, 520, 519, 368, 367, 429, 428) 
		AND tmp_acceso >= '%s' 
		GROUP BY 2 
		HAVING COUNT(*) > %s) 
	select count(distinct(txt_matricula)) 
		FROM public.t_transito t 
			JOIN public.mv_vehiculo_distintivo_ambiental mvda USING ( txt_matricula ) 
			JOIN habituales USING ( txt_matricula ) JOIN public.t_sancion s USING ( cod_transito ) 
		WHERE s.cod_estado_sancion in ( 5, 1 ) 
			AND t.cod_pdc <> 116
			AND mvda.cod_distintivo_ambiental <> 9 
			AND s.fec_sancion >= '%s'"""
