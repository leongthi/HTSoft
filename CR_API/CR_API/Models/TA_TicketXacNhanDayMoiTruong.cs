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
    using System.Collections.Generic;
    
    public partial class TA_TicketXacNhanDayMoiTruong
    {
        public long TicketID { get; set; }
        public Nullable<int> UserIDConfirm { get; set; }
        public string Confirmer { get; set; }
        public Nullable<System.Guid> MoiTruongID { get; set; }
        public string MoiTruongName { get; set; }
        public Nullable<System.DateTime> CreatedOn { get; set; }
        public Nullable<System.Guid> CreatedBy { get; set; }
        public Nullable<System.DateTime> ModifiedOn { get; set; }
        public Nullable<System.Guid> ModifiedBy { get; set; }
    }
}