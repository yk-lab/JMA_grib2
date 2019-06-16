import numpy as np

from .jmagpv import JMAGPV

class Ggis1km(JMAGPV):
    """
    1km メッシュ全国合成レーダー GPV クラス。

    Attributes
    ----------
    section0 : Section0
        第 0 節の情報。
    section1 : Section1
        第 1 節の情報。
    section3 : Section3
        第 3 節の情報。
    section4 : Section4
        第 4 節の情報。
    section5 : Section5
        第 5 節の情報。
    section6 : Section6
        第 6 節の情報。
    section7 : Section7
        第 7 節の情報。
    data : np.array
        メインデータ。
    """

    class Section0:
        """
        第 0 節。

        Attributes
        ----------
        name : int
            節番号。
        grib : str
            "GRIB"。
        document_field : int
            資料分野。 (0=気象分野)
        grib_version : int
            GRIB 版番号。(2)
        bytes_length : int
            GRIB 報全体のバイト数。
        """

        name = 0
        def __init__(self, grib, _, document_field, grib_version, bytes_length):
            self.grib = grib
            self.document_field = document_field
            self.grib_version = grib_version
            self.bytes_length = bytes_length

    class Section1:
        """
        第 1 節。

        Attributes
        ----------
        name : int
            節番号。
        length : int
            節のバイト数。
        center : int
            作成中枢の識別。 (34=東京)
        secondary_center : int
            作成副中枢。(0)
        grib_master_version : int
            GRIB マスター表バージョン番号。(2)
        grib_local_version : int
            GRIB 地域表バージョン番号。(1)
        reference_time : int
            参照時刻の意味。(0=解析)
        document_datetime : datetime
            資料の参照時刻(UTC)。
        create_status : int
            作成ステータス。(0=現業プロダクト)
        document_type : int
            資料の種類。(0=解析プロダクト)
        """

        name = 1
        def __init__(self, length, center, secondary_center, grib_master_version, grib_local_version,
                     reference_time, document_datetime, create_status, document_type):
            self.length = length
            self.center = center
            self.secondary_center = secondary_center
            self.grib_master_version = grib_master_version
            self.grib_local_version = grib_local_version
            self.reference_time = reference_time
            self.document_datetime = document_datetime
            self.create_status = create_status
            self.document_type = document_type

    class Section3:
        """
        第 3 節。
        """

        name = 3
        def __init__(self, length, lattice_system, num_of_points, _a, _b, lattice_system_definition_template_num,
                     earth_shape, _c, _d,
                     long_axis_scale_factor, long_axis_scale_length, short_axis_scale_factor, short_axis_scale_length,
                     lat_points, lng_points, base_angle, _e, first_lat, first_lng, resolution_and_component_flag,
                     last_lat, last_lng, incremental_i, incremental_j, scanning_mode):
            self.length = length
            self.lattice_system = lattice_system
            self.num_of_points = num_of_points
            self.lattice_system_definition_template_num = lattice_system_definition_template_num
            self.earth_shape = earth_shape
            self.long_axis_scale_factor = long_axis_scale_factor
            self.long_axis_scale_length = long_axis_scale_length
            self.short_axis_scale_factor = short_axis_scale_factor
            self.short_axis_scale_length = short_axis_scale_length
            self.lat_points = lat_points
            self.lng_points = lng_points
            self.base_angle = base_angle
            self.first_lat = first_lat
            self.first_lng = first_lng
            self.resolution_and_component_flag = resolution_and_component_flag
            self.last_lat = last_lat
            self.last_lng = last_lng
            self.incremental_i = incremental_i
            self.incremental_j = incremental_j
            self.scanning_mode = scanning_mode

    class Section4:
        """
        第 4 節。
        """

        name = 4
        def __init__(self, length, _a, product_template_num, param_category, param_num, processing_type,
                     value_type, _b, _c, _d, _e, _f, first_fixed_surface_type, _g, _h, _i, _j, _k,
                     all_timedelta_finish_datetime, _l, _m, statistical_processing_type,
                     statistical_processing_unit, statistical_processing_timedelta, _n, _o, _p,
                     radar_operation_info, rf_conversion_factor_operation_info, _q):
            self.length = length
            self.product_template_num = product_template_num
            self.param_category = param_category
            self.param_num = param_num
            self.processing_type = processing_type
            self.value_type = value_type
            self.first_fixed_surface_type = first_fixed_surface_type
            self.all_timedelta_finish_datetime = all_timedelta_finish_datetime
            self.statistical_processing_type = statistical_processing_type
            self.statistical_processing_unit = statistical_processing_unit
            self.statistical_processing_timedelta = statistical_processing_timedelta
            self.radar_operation_info = radar_operation_info
            self.rf_conversion_factor_operation_info = rf_conversion_factor_operation_info

    class Section5:
        """
        第 5 節。
        """

        name = 5
        def __init__(self, length, num_of_all_document_points, document_template_num, num_of_bits_by_one_data,
                     max_level_value, _a, data_representative_value, level_data_representative_value):
            self.length = length
            self.num_of_all_document_points = num_of_all_document_points
            self.document_template_num = document_template_num
            self.num_of_bits_by_one_data = num_of_bits_by_one_data
            self.max_level_value = max_level_value
            self.data_representative_value = data_representative_value
            self.level_data_representative_value = np.array(level_data_representative_value)/(10**self.data_representative_value)

    class Section6:
        """
        第 6 節。
        """

        name = 6
        def __init__(self, length, bitmap_indicator):
            self.length = length
            self.bitmap_indicator = bitmap_indicator

    class Section7:
        """
        第 7 節。
        """

        name = 7
        def __init__(self, length, run_length_octet_strings):
            self.length = length
            self.run_length_octet_strings = run_length_octet_strings

    def read(self):
        """
        1km メッシュ全国合成レーダー GPV GRIB2 ファイルを読み込む。
        """

        b  = self.r  # bytes 型
        i  = self.r_int  # int 型
        s  = self.r_str  # str 型
        dt = self.r_dt  # datetime 型

        # 第 0 節
        self.section0 = Ggis1km.Section0(s(1,4), i(5,6), i(7), i(8), i(9, 16))
        # 第 1 節
        sec_length = i(1,4)
        sec_name = i(5)
        assert sec_name == 1
        self.section1 = Ggis1km.Section1(sec_length, i(6,7), i(8,9), i(10), i(11), i(12), dt(13), i(20), i(21))
        # 第 3 節
        sec_length = i(1,4)
        sec_name = i(5)
        assert sec_name == 3
        self.section3 = Ggis1km.Section3(sec_length, i(6), i(7, 10), i(11), i(12), i(13,14), i(15), i(16),
                                         i(17, 20), i(21),i(22, 25), i(26), *[i(27, 30) for _ in range(7)],
                                         i(55), *[i(56, 59) for _ in range(4)], i(72))
        # 第 4 節
        sec_length = i(1,4)
        sec_name = i(5)
        assert sec_name == 4
        self.section4 = Ggis1km.Section4(sec_length, i(6,7), i(8,9), *[i(10) for _ in range(10, 15)],
                                         i(15,16), i(17), i(18), i(19,22), i(23), i(24), i(25,28), i(29), i(30),
                                         i(31,34), dt(35), i(42), i(43,46), i(47), i(48), i(49), i(50,53), i(54),
                                         i(55,58), *[i(59,66) for _ in range(3)])
        # 第 5 節
        sec_length = i(1,4)
        sec_name = i(5)
        assert sec_name == 5
        self.section5 = Ggis1km.Section5(sec_length, i(6,9), i(10,11), i(12), i(13,14), i(15,16), i(17),
                                         [i(16+2*nn,17+2*nn) for nn in range(1, 252)])
        # 第 6 節
        sec_length = i(1,4)
        sec_name = i(5)
        assert sec_name == 6
        self.section6 = Ggis1km.Section6(sec_length, i(6))
        # 第 7 節
        sec_length = i(1,4)
        sec_name = i(5)
        assert sec_name == 7
        self.section7 = Ggis1km.Section7(sec_length, b(6,sec_length))
        self.data = self.decode_rle(self.section7.run_length_octet_strings, 8, self.section5.max_level_value, self.section5.level_data_representative_value)
        flag = b(1,4)
        assert flag.decode() == '7777'

    @classmethod
    def decode_rle(cls, b, nbit, maxv, level_value, column=2560, row=3360):
        data = super(Ggis1km, cls).decode_rle(b, nbit, maxv, column, row)
        level_value = np.concatenate(([np.nan], level_value))
        return np.vectorize(lambda x: level_value[x])(data)
