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
    
    public partial class RequirementOriginal
    {
        public long Seq { get; set; }
        public string RequirementCode { get; set; }
        public Nullable<int> BuilID { get; set; }
        public string Detail { get; set; }
        public Nullable<System.DateTime> Deadline { get; set; }
        public string Note { get; set; }
        public string Module { get; set; }
        public string TypeRequirement { get; set; }
        public Nullable<int> ClientID { get; set; }
        public string URDID { get; set; }
        public string URDFileName { get; set; }
        public Nullable<System.DateTime> CreatedOn { get; set; }
        public Nullable<int> CreatedBy { get; set; }
        public Nullable<System.DateTime> ModifiedOn { get; set; }
        public Nullable<int> ModifiedBy { get; set; }
    }
}