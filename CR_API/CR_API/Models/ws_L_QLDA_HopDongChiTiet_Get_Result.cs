//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated from a template.
//
//     Manual changes to this file may cause unexpected behavior in your application.
//     Manual changes to this file will be overwritten if the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

namespace CR_API.Models
{
    using System;
    
    public partial class ws_L_QLDA_HopDongChiTiet_Get_Result
    {
        public Nullable<int> MaDA { get; set; }
        public Nullable<int> Nam { get; set; }
        public string ContractNumber { get; set; }
        public Nullable<System.DateTime> ContractDate { get; set; }
        public Nullable<bool> UseYear { get; set; }
        public Nullable<bool> UseMonth { get; set; }
        public Nullable<int> MaThoiHan { get; set; }
        public Nullable<System.DateTime> NgayKetThuc { get; set; }
        public Nullable<System.DateTime> NgayPhuLuc { get; set; }
        public string MaLoaiHD { get; set; }
        public string MaLoaiTien { get; set; }
        public Nullable<decimal> GiaTriHopDong { get; set; }
        public string GhiChu { get; set; }
    }
}